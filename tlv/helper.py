import sys


def debug(args, msg):
    if args.verbose:
        print(msg)


def die(code, msg=None):
    if msg:
        if not msg.endswith("\n"):
            msg += "\n"
        sys.stderr.write(msg)
    sys.exit(code)
