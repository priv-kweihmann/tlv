import multiprocessing as mp
import os
from copy import deepcopy
from difflib import SequenceMatcher
from itertools import permutations

import chardet
from pygments import lexers
from pygments.util import ClassNotFound

from tlv.cls_ast import TLVAst
from tlv.cls_ast import TLVFinding
from tlv.helper import debug
from tlv.helper import die


def parse(args):
    res = []
    for f in args.files:
        if not os.path.isfile(f):
            continue
        _lexer = None
        if args.lexer:
            try:
                _lexer = lexers.get_lexer_by_name(args.lexer)
            except ClassNotFound:
                die(-1, "Lexer '{lex}' isn't available can't proceed".format(lex=args.lexer))
        else:
            try:
                _lexer = lexers.get_lexer_for_filename(f)
            except ClassNotFound:
                continue
        debug(args, "Reading {f}".format(f=f))
        with open(f, "rb") as i:
            try:
                content = i.read()
                _enc = chardet.detect(content)
                content = content.decode(_enc["encoding"]).encode("utf-8")
                _ast = TLVAst(f)
                res.append(_ast)
                for x in _lexer.get_tokens(content):
                    _type, _value = x
                    if str(_type) in args.wildcard_token:
                        _ast.Processed.append((_type, ""))
                    else:
                        _ast.Processed.append((_type, _value))
                    _ast.Raw.append(x)
            except UnicodeDecodeError:
                continue
    return res


def __evaluate(args, first, second):
    findings = []
    debug(args, "Comparing {a}<>{b}".format(a=os.path.basename(
        first.Filename), b=os.path.basename(second.Filename)))
    m = SequenceMatcher(None, first.Processed,
                        second.Processed).get_matching_blocks()
    for _m in m:
        _id = TLVFinding.Validate(args, first, second, _m)
        if _id:
            findings.append(TLVFinding(first, second, _m, _id))
            findings.append(TLVFinding(second, first, _m, _id))
    return findings


def validate(args, _list):
    perms = permutations(_list, 2)
    results = []
    with mp.Pool(processes=args.jobs) as pool:
        results = [pool.apply(__evaluate, args=(args, first, second))
                   for first, second in perms]
    # append one time every file compared against it self
    # by cutting the content into half
    for x in _list:
        _x1 = deepcopy(x)
        _x2 = deepcopy(x)
        chop_point = int(len(_x1.Raw) / 2)
        if chop_point > 0:
            _line_offset = TLVFinding.get_text(
                _x1, 0, chop_point).count(os.linesep)
            _x1.Raw = _x1.Raw[0: chop_point]
            _x1.Processed = _x1.Processed[0: chop_point]
            _x2.Raw = _x2.Raw[chop_point:]
            _x2.Processed = _x2.Processed[chop_point:]
            _x2.LineOffset = _line_offset
            results.append(__evaluate(args, _x1, _x2))
    return list(set([item for sublist in results for item in sublist]))  # noqa: C403
