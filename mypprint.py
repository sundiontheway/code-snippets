#coding: utf-8
"""A script which can show beautiful print from OSX clipboard.
"""

import pprint
import commands


def main():
    out = ''
    string = commands.getoutput("pbpaste")
    pp = pprint.PrettyPrinter(indent=4)
    try:
        out = eval(string)
    except:
        pp.pprint(string)

    if not isinstance(out, dict):
        pp.pprint(string)
    pp.pprint(out)

if __name__ == "__main__":
    main()
