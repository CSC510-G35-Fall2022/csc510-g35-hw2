import csv
class num:
    def __init__(self,name,_has):
        n=0
        at=len(self._has)
        name=self.name
        _has=self._has
        lo=min(self._has) if len(self._has)>1 else 0
        hi=min(self._has) if len(self._has)>1 else 0
        isSorted=False
    def nums():
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has
    def div(a):
        a=self.nums()
        mean = sum(a)/len(a)
        variance = sum([((x - mean) ** 2) for x in a]) / len(a)
        stddev = variance ** 0.5
        return(stddev)
    def median(a):
        a=self.nums()
        return(a[len(a)//2])