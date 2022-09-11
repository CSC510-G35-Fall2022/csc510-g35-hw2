import sys

import os
fpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'code')
sys.path.append(fpath)
#print(sys.path)

import commandLine as c
from num import num as Num
from sym import Sym as Sym

class Test:

    eg, fails = {}, 0

    def __init__(self):
        self.message = 'yo'

    def the(self):
        print('the test')
        print(c.the)
        return True

    def bignum(self):
        num = Num("Hello")
        print('bignumtest')
        c.the["nums"] = 32
        for i in range(1000):
            num.add(i, i)
        print(Num.nums())
        print(32 == num._has)

    def num(self):

        num= Num("hello")
        c.the["nums"] = 32
        for i in range(100):
            num.add(i, i)
        mid, div = num.median(), num.div()
        print(mid, div)
        print(32 == num._has)

    def sym(self):
 
        sym= Sym("sym")
        c.the["nums"] = 32
        for x,y in sym._has:
            sym.add(y)
        mode, entropy = sym.mid(), sym.div()
        print(mid, div)
        print(32 == sym._has)

instance = Test()
instance.the()
print("Num test")
instance.num()
print("Sym test")
instance.sym()