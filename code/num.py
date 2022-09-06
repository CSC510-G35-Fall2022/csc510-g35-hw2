import csv
import random
import utilities
import commandLine as c

class num:
    def __init__(self,name,_has):
        self.n=0
        self.at=len(_has)
        self.name=name
        self._has=_has
        self.lo=min(_has) if len(_has)>1 else 0
        self.hi=min(_has) if len(_has)>1 else 0
        self.isSorted=False
    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has
    def add(self,v,posi):
        if v!="?":
            self.n=self.n+1
            self.lo=min(v,self.lo)
            self.hi=max(v,self.hi)
            if len(self._has)< c.the["nums"]:
                pos=1+ len(self._has)
            elif random.randrange(0,1)< c.the["nums"]:
                pos=1+random.randint(0, len(self._has))
            if pos:
                self.isSorted=False
                self._has[pos]=v

        
    def div(self, a):
        a=self.nums()
        mean = sum(a)/len(a)
        variance = sum([((x - mean) ** 2) for x in a]) / len(a)
        stddev = variance ** 0.5
        return(stddev)
    def median(self, a):
        a=self.nums()
        return(a[len(a)//2])
utilobj=utilities.utilities()
print(utilobj.get_num_data())