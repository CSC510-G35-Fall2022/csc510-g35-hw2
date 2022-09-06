import sys

import os
fpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'code')
sys.path.append(fpath)
#print(sys.path)

import commandLine as c
from num import num as Num

class Test:

    eg, fails = {}, 0

    def __init__(self):
        self.message = 'yo'

    def the(self):
        print(c.the)
        return True

    def bignum(self, num):
        num = Num("hello", {1, 2, 3})
        c.the["nums"] = 32
        for i in range(1000):
            num.add(i, i)
        print(Num.nums())
        print(32 == num._has)

instance = Test()
instance.the()