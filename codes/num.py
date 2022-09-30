import random as r
import math
from codes.utilities import utilities as u
import codes.commandLine as c
class Num:
    '''Holds number cols and applies functions to them'''
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

    def nums(self):
        '''
        Sorts the has list and sets isSorted to True
        '''
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has

    def add(self, v):
        ''' 
        Adds a new value to the list and replaces a random old value if size exceeds attribute defined by the["nums"] config
        
        :param v: value to add to the list

        '''
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
    
    def div(self):
        '''
        Returns the diversity of the nums object
        :return: diversity of sym object
        '''
        a=self.nums()
        return (u.per(a, 0.9) - u.per(a, 0.1)) / 2.58

    '''
    Returns the median of the nums object
    '''
    def mid(self):
        '''
        Returns the median of the nums col

        :return: median of nums list

        '''
        return u.per(self.nums(), 0.5)

    def __string__(self):
        return 'at: {0} hi: {1} isSorted: {2} lo: {3} n: {4} name: {5} w: {6}'.format(self.at, self.hi, self.isSorted, self.lo, self.n, self.name, self.w)