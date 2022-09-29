import sys
import os
sys.path.insert(0, os.getcwd())

print(sys.path)
from codes import cols
from codes.num import Num
from codes.sym import Sym
import codes.utilities as u
from codes.data import Data
import codes.commandLine as c

import random

class Test:
    def the(self):
        print(c.the)
        return True
        
   

    def __init__(self):
        self.message = 'yo'

    def datatest(self):
        filename='hw2test.csv'
        data = Data(filename)
        l=list(data.cols.y)
        return True if len(l)==3 else False

    def bignum(self):
        num = Num(0, "Hello")
        print('bignumtest')
        c.the["nums"] = 32
        for i in range(1, 1001):
            num.add(i)
        print(num.nums())
        return 32 == len(num._has)

    def num(self):
        num = Num(0, "hello")
        for i in range(1,101):
            num.add(i)
        print(num.nums())
        mid, div = num.median(), num.div()
        print(mid, div)
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

    def sym(self):
        sym= Sym(0, "Hello")
        c.the["nums"] = 32
        for x in ["a","a","a","a","b","b","c"]:
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        return mode == "a" and 1.37 <= entropy and entropy <=1.38
    
    
    
    eg, fails = {'the': the, "num": num, "bignum": bignum, "sym": sym, "data":datatest}, 0

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

    def all(self):
        for k, v in self.eg.items():
            self.runs(k)
        


instance = Test()
instance.the()
instance.all()
#print("Num test")
#print(instance.num())
#print(instance.bignum())
#print("Sym test")
#print(instance.sym())
#data = Data("hw2test.csv")
# for y in data.cols.x:
#     print("Name: {0} column: {1}".format(y.name, y._has))