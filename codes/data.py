from codes.utilities import utilities as u
import sys
from itertools import chain
from codes.cols import Cols
from codes.row import Row
import codes.utilities as u1
the = {"nums": 512, "seperator": ','}
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
        sep=the['seperator']

        if isinstance(src, str):
            u1.csvs(src, self.add)
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
        self.places= places or 2
        self.show_cols=show_cols or show_cols.x
        self.fun= fun or "mid"
        table={}
        for col in show_cols:
            if fun=="mid":
                val=col.mid()
            else:
                val=col.div()
            value= round(value, places)
            table[col.name]=value
        return table