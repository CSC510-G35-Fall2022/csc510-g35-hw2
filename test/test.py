import sys

import os
fpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'code')
sys.path.append(fpath)
#print(sys.path)

import commandLine as c
from num import Num as Num
from sym import Sym as Sym

class Test:

    eg, fails = {}, 0

    def __init__(self):
        self.message = 'yo'

    def the(self):
        print(c.the)
        return True

    def bignum(self):
        num = Num(0, "Hello")
        print('bignumtest')
        c.the["nums"] = 32
        for i in range(1, 1001):
            num.add(i, i - 1)
        print(num.nums())
        return 32 == len(num._has)

    def num(self):
        num = Num(0, "hello")
        for i in range(1,101):
            num.add(i, i - 1)
        print(num.nums())
        mid, div = num.median(), num.div()
        print(mid, div)
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

    def sym(self):
        sym= Sym(0,"Hello")
        c.the["nums"] = 32
        for x in ["a","a","a","a","b","b","c"]:
            sym.add(y)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        return mode == "a" and 1.37 <= entropy and entropy <=1.38


instance = Test()
instance.the()
#print("Num test")
print(instance.num())
print(instance.bignum())
#print("Sym test")
print(instance.sym())