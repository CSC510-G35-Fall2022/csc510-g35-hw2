from logging import NullHandler
from codes.num import Num
from codes.sym import Sym
import codes.utilities as u
import re

class Cols:
    '''Declares a column class that holds a column of data'''

    def __init__(self, names):
        ''' 
        inits Cols with name of col

        :param names: (str) first row containing names of the columns
        :type names: (str) names of the columns
        :type all: (list[col]) every column including skipped columns are included here
        :type klass: (col) single dependent col
        :type x: (list[col]) every independent unskipped column
        :type y: (list[col]) every dependent unskipped column
        
        '''
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for c, s in enumerate(names):
            col = Num(c, s) if s[0].isupper() else Sym(c, s)
            self.all.append(col)
            if s[-1] != ':':
                if s.find('+') != -1 or s.find('-') != -1:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if s[-1] == '!':
                    self.klass = col


