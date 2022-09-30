import random as r
import math
from codes.utilities import utilities as u
import codes.commandLine as c
class Num:
    '''
    Parameters:
    c = column position
    s = column name
    Attributes:
    n = size
    name = name
    has = list of numbers associated with Num object
    at = column position
    lo = lowest number
    hi = highest number
    isSorted = Boolean represented if sorted
    '''
    def __init__(self, c, s):
        self.n = 0
        self.name = s
        self._has = []
        self.at = c or 0
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted=True
        if s[-1] == '-':
            self.w = -1
        else:
            self.w = 1

    """
    Sorts the has list and sets isSorted to True
    """
    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has

    '''
    v = value
    pos = position
    Adds a new value to the list
    replaces a random old value if size 
    exceeds attribute defined by the["nums"] config
    '''
    def add(self, v):
        #print(v)
        v = float(v)
        if v!="?":
            self.n = self.n + 1
            self.lo = min(float(v), self.lo)
            self.hi = max(float(v), self.hi)
            if len(self._has) < c.the["nums"]:
                pos = len(self._has)
                self._has.insert(pos, v)
            elif r.random() < c.the["nums"] / self.n:
                pos = r.randrange(len(self._has))
                self._has[pos] = v
            self.isSorted = False
        
    '''
    Returns the diversity of the nums object
    NOT to be confused with the usual "standard deviation"
    involves taking the 90th and 10th percentile values and dividing by 2.58
    '''
    def div(self):
        a=self.nums()
        return (u.per(a, 0.9) - u.per(a, 0.1)) / 2.58

    '''
    Returns the median of the nums object
    '''
    def mid(self):
        return u.per(self.nums(), 0.5)

    def __string__(self):
        return 'at: {0} hi: {1} isSorted: {2} lo: {3} n: {4} name: {5} w: {6}'.format(self.at, self.hi, self.isSorted, self.lo, self.n, self.name, self.w)