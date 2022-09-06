import csv
import random
import utilities
class num:
    def __init__(self,name,_has):
        n=0
        at=len(self._has)
        name=self.name
        _has=self._has
        lo=min(self._has) if len(self._has)>1 else 0
        hi=min(self._has) if len(self._has)>1 else 0
        isSorted=False
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
            if len(self._has)< maxlim:
                pos=1+ len(self._has)
            elif random.randrange(0,1)< maxlim/n:
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
