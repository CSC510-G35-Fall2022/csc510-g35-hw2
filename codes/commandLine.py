import sys
import re 
from codes.utilities import utilities as u


#default values
help = "USAGE: py commandLine.py [OPTIONS]\n\n\
-e --eg    start-up example    = nothing\n\
-d --dump   on test failure, exit with stack dump = false\n\
-f --file with csv data = ../data/auto93.csv\n\
-h --help   show help   = false\n\
-n --nums   number of nums to keep  = 512\n\
-s --seed   random number seed  = 10019\n\
-S --seperator feild seperator = ,\n\n\
-- Function argument conventions:\n\
-- 1. two blanks denote options, four blanks denote locals:\n\
-- 2. prefix n,s,is,fun denotes number,string,bool,function;\n\
-- 3. suffix s means list of thing (so names is list of strings)\n\
-- 4. c is a column index (usually)"
arg = sys.argv[1:]

the = {}
#compile pattern with help and turn into dictionary
pattern = re.compile("\n[-][\S]+[\s]+[-][-]([\S]+)[^\n]+=[\s]([\S]+)")
for match in pattern.finditer(help):
    k, v = match.group(1, 2)
    the[k] = u.coerce(v)

"""
Reads in default options and stores in configuration dictionary "the"
t = dictionary of options
"""
def cli(t):
    for slot, v in t.items():
        v = str(v)
        for n, x in enumerate(arg):
            if x == "-" + slot[0] or x == "--" + slot:
                v = v == "false" and "true" or v == "true" and "false" or arg[n + 1]
        t[slot] = u.coerce(v)
    if len(sys.argv) == 2 and arg[0] == "help":
        print("\n" + help + "\n")
        exit()
    return t     

the = cli(the)
#print(the)
