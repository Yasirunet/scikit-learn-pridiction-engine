#!/usr/bin/env python
def get_value(*args):
    return "Hello World " + ":".join(map(str, args))

def main(argv):
    print(get_value(*argv[1:]))

if __name__ == "__main__":
    import sys
    main(sys.argv)