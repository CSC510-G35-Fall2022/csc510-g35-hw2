from . import utilities as u
from .cols import Cols
from .row import Row

class Data:
    '''
    Parameters:
    src = location of the csv file to import from
    Attributes:
    cols = summary of data
    rows = list of rows
    '''
    def __init__(self, src):
        self.cols = None
        self.rows = []
        u.csvs(src, self.add)

    '''
    xs = row to insert
    '''
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs)
        else: 
            self.rows.append(xs)