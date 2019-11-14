from tlv.arg_parser import ArgParser
from tlv.src_parser import parse
from tlv.src_parser import validate

if __name__ == '__main__':
    args = ArgParser()
    res = validate(args, parse(args))
    for r in res:
        r.Print(args)
