import argparse
import os

from tlv.lexer import LEXERS
from tlv.tokens import TOKENS

RUNARGS = None


def ArgParser():
    parser = argparse.ArgumentParser(
        prog="tlv", description='Find code duplications across various languages')
    parser.add_argument("--minlines", type=int, default=5,
                        help="Minimum length of block in lines before reporting")
    parser.add_argument("--mintoken", type=int, default=20,
                        help="Minimum length of block in token before reporting")
    parser.add_argument("-j", "--jobs", type=int, default=1,
                        help="Number of jobs to run in parallel")
    parser.add_argument("--lexer", choices=LEXERS, default=None,
                        help="Manually set a lexer to use on all files")
    parser.add_argument("--wildcard_token", choices=TOKENS, action='append',
                        default=[
                            "Token.Comment.Multiline",
                            "Token.Comment.Preproc",
                            "Token.Literal.Number",
                            "Token.Literal.Number.Bin",
                            "Token.Literal.Number.Float",
                            "Token.Literal.Number.Hex",
                            "Token.Literal.Number.Integer",
                            "Token.Literal.Number.Integer.Long",
                            "Token.Literal.Number.Oct",
                            "Token.Text",
                            "Token.Whitespace",
                        ],
                        help="Token types that are threated as wildcards (actual value doesn't matter)")
    parser.add_argument("--verbose", default=False,
                        action="store_true", help="Verbose output")
    parser.add_argument("--nodetails", default=True, action="store_false",
                        dest="details", help="Dump the details of a finding")
    parser.add_argument("files", nargs='+', help="Files to parse")
    RUNARGS = parser.parse_args()
    # Turn all paths to abs-paths right here
    RUNARGS.files = [os.path.abspath(x) for x in RUNARGS.files]
    return RUNARGS
