from ctypes import util
from codes.utilities import utilities
import math
class Sym:
    
    def __init__(self, c, s):
        self.n = 0
        self.name = s
        self._has = {}
        self.at = c or 0

    def add(self,v):
        if v!="?":
            self.n=self.n+1
        if v in self._has:
            self._has[v]= 1+(self._has[v] or 0)
        else:
            self._has[v]= 1

    def fun(self,p):
        return p*math.log(p,2)

    def div(self):
        e=0
        for k,v in self._has.items():
            if v>0:
                e=e-self.fun(v/self.n)
        return e
        
    #finds mode of a column of data in the sym class
    def mid(self):
        most = -1
        mode = None
        for k,v in self._has.items():
            if v > most:
                most = v
                mode = k
        return mode


# utilobj=utilities.utilities()
# data_dict = utilobj.convert_data_list_to_dict(utilobj.get_sym_data())
# print("xmid: ", Sym.mid(data_dict))

