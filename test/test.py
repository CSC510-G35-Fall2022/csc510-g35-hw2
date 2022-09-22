import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import code
import code.commandLine as c
from code.num import Num
from code.sym import Sym
import code.utilities as u
from code.data import Data
import math
import random

class Test:
    def the(self):
        print(c.the)
        return True
        
   

    def __init__(self):
        self.message = 'yo'

   

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
    
    
    eg, fails = {'the': the, "num": num, "bignum": bignum, "eg": 0, "nothing": 0}, 0

    def runs(self, k):
        if  k not in self.eg.keys():
            print('returning')
            return
       
        c.the['seed'] = random.random()
        old = {}
        for x,y in c.the.items():
            old[x] = y
        status, out = False, False
        if c.the['dump']:
            status=True
            out = self.eg[k](self)
        else: 
            try:
                out= self.eg[k](self)
            except:
                status=False
        
        for x,y in old.items(): 
            c.the[k] = y

        msg =  ("PASS" if out else "FAIL") if status else "CRASH"
        print("!!!!!!\t" + msg +"\t" + k + "\t" + str(status))
        


instance = Test()
instance.the()
instance.runs("bignum")
#print("Num test")
#print(instance.num())
#print(instance.bignum())
#print("Sym test")
#print(instance.sym())
data = Data("../hw2test.csv")
# for y in data.cols.x:
#     print("Name: {0} column: {1}".format(y.name, y._has))