import csv
import pprint as pp
from webbrowser import get
import math
import re

# Read csv file with a comma as the delimiter, then split the data according
# to num, sy and dependent data
csvfile = open('../hw2test.csv', 'r')
datalist = []
for row in csv.reader(csvfile, delimiter=","):
    datalist.append(row)

allcols = []
alldict = {}

numcols = []
numdict = {}

symcols = []
symdict = {}

depcols = []
depdict = {}

indepcols = []
indepdict = {}

# split the data according to num and sym definitions
ct = 0
for i in datalist[0]:
    allcols.append(i)
    alldict[i] = ct

    if i[0].isupper() and i[-1] != '+' and i[-1] != '-' and i[-1] != ':':
        numcols.append(i)
        indepcols.append(i)

        numdict[i] = ct
        indepdict[i] = ct

    if i[0].islower() and i[-1] != '+' and i[-1] != '-' and i[-1] != ':':
        symcols.append(i)
        indepcols.append(i)

        symdict[i] = ct
        indepdict[i] = ct

    if  i[-1] == '-' or i[-1] == '+':
        depcols.append(i)
        depdict[i] = ct

    ct += 1


num_data_list = []
sym_data_list = []
dep_data_list = []
indep_data_list = []
all_data_list = []

for idx in range (0, len(datalist)):
    tmp_num = []
    tmp_sym = []
    tmp_dep = []
    tmp_indep = []
    tmp_all = []
    for x in range (0, len(datalist[idx])):
        tmp_all.append(datalist[idx][x])

        if x in list(numdict.values()):
            tmp_num.append(datalist[idx][x])
            tmp_indep.append(datalist[idx][x])

        if x in list(symdict.values()):
            tmp_sym.append(datalist[idx][x])
            tmp_indep.append(datalist[idx][x])

        if x in list(depdict.values()):
            tmp_dep.append(datalist[idx][x])
    
    num_data_list.append(tmp_num)
    sym_data_list.append(tmp_sym)
    dep_data_list.append(tmp_dep)
    indep_data_list.append(tmp_indep)
    all_data_list.append(tmp_all)


'''
t = sorted list
p = percentile
Returns a number located at the pth percentile location in the sorted list t
'''
def per(t, p):
    n = len(t)
    #obtains position based off percentile
    p = math.floor((p or 0.5) * n + 0.5);
    return t[max(1, min(n, p)) - 1]

def copy():
    return "test"

def csvs(fname, fun):
    sep = ','
    src = open(fname)
    for line in src:
        t = []
        #TODO add coerce function here later
        for s1 in line.rstrip().split(sep):
            t.append(s1)
        fun(t)




# utilities class which holds functions go get data as a 2D list and 
# another function to convert the 2D list data into a dictionary format.
class utilities:
    #CSV Function from the code
    def csv(self, fname, fun):
        #print("Inside CSV Function in utilities")
        src= open(fname)
        s=src.readline()
        while s:
            line=s.strip()
            t=line.split(",")
            s=src.readline()

    # get num data as a 2D array
    def get_num_data(self):
        return num_data_list

    # get sym data as a 2D array
    def get_sym_data(self):
        return sym_data_list

    # get dependent data (y) as a 2D array
    def get_dep_data(self):
        return dep_data_list

    # get independent (x) data as a 2D array
    def get_indep_data(self):
        return indep_data_list

    # get all data as a 2D array
    def get_all_data(self):
        return all_data_list

    # convert 2D array data into a dictionary
    def convert_data_list_to_dict(self, data_):
        tmp_dict = {}
        for x in range(0, len(data_[0])):
            tmp_dict[data_[0][x]] = []

        for i in range(1, len(data_)):
            for j, key in enumerate(tmp_dict.keys()):
                tmp_dict[key].append(data_[i][j])

        return tmp_dict
utiltest=utilities()
utiltest.csv("../hw2test.csv",'a')