from codes.utilities import utilities as u
import sys
from itertools import chain
from codes.cols import Cols
from codes.row import Row
import codes.utilities as u1
import math

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
        self.src=src

        if isinstance(src, str):
            u1.csvs(src, self.add, False)
        else:
            for row in enumerate(src or []):
                self.add(row)

    '''
    xs = row to insert
    '''
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row=u1.push(self.rows, Row(xs))
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.at])

    def stats(self, places, show_cols, fun):
        table={}
        for col in show_cols:
            v = fun(col)
            if type(v) == int or type(v) == float:
                mult = 10**places
                v = math.floor(v * mult + 0.5) / mult
            table[col.name] = v
        return table