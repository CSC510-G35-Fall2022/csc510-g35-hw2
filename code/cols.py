from logging import NullHandler
from . import utilities as u
from .num import Num
from .sym import Sym
import re

#store csv data, get functions for each
class Cols:
    #single dependent klass column - dont know what this is
    '''
    Parameters:
    names = first row containing names of the columns
    Attributes:
    names = names of the columns
    all = every column including skipped columns are included here
    klass = single dependent col?
    x = every dependent unskipped column
    y = every independent unskipped column
    '''
    def __init__(self, names):
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
                    self.x.append(col)
                else:
                    self.y.append(col)
                if s[-1] == '!':
                    self.klass = col


