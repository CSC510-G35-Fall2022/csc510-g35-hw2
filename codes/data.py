from codes.utilities import utilities as u
import sys
from itertools import chain
from codes.cols import Cols
from codes.row import Row
import codes.utilities as u1
import math

class Data:
    '''Declares a data class that holds col and row data'''

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

    def add(self, xs):
        '''
        Adds a row and appends to any columns

        :param xs: row to add

        '''
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row=u1.push(self.rows, Row(xs))
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.at])

    def stats(self, places, show_cols, fun):
        '''
        Shows stats for each col based on input function

        :param places: rounding int
        :param show_cols: list of columns
        :param fun: function to apply to each column
        :return: dictionary of column stats

        '''
        table={}
        for col in show_cols:
            v = fun(col)
            if type(v) == int or type(v) == float:
                mult = 10**places
                v = math.floor(v * mult + 0.5) / mult
            table[col.name] = v
        return table