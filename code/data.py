from . import utilities as u
from itertools import chain
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
            if not isinstance(xs, Row):
                row = Row(xs)
            else:
                row = xs
            self.rows.append(row)
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.at])

    def stats(self, places):
        return "hi"
