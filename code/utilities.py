import csv
import pprint as pp
from webbrowser import get


csvfile = open('/Users/mayapatel/Documents/Academics/Fall 2022/CSC510/csc510-g35-hw2/hw2test.csv', 'r')
datalist = []
for row in csv.reader(csvfile, delimiter=","):
    datalist.append(row)

numcols = []
numdict = {}
symcols = []
symdict = {}
depcols = []
depdict = {}

ct = 0
for i in datalist[0]:
    if i[0].isupper() and i[-1] != '+' and i[-1] != '-' and i[-1] != ':':
        numcols.append(i)
        numdict[i] = ct
    if i[0].islower() and i[-1] != '+' and i[-1] != '-' and i[-1] != ':':
        symcols.append(i)
        symdict[i] = ct
    if  i[-1] == '-' or i[-1] == '+':
        depcols.append(i)
        depdict[i] = ct
    ct += 1


num_data_list = []
sym_data_list = []
dep_data_list = []

for idx in range (0, len(datalist)):
    tmp_num = []
    tmp_sym = []
    tmp_dep = []
    for x in range (0, len(datalist[idx])):
        if x in list(numdict.values()):
            tmp_num.append(datalist[idx][x])
        if x in list(symdict.values()):
            tmp_sym.append(datalist[idx][x])
        if x in list(depdict.values()):
            tmp_dep.append(datalist[idx][x])
    
    num_data_list.append(tmp_num)
    sym_data_list.append(tmp_sym)
    dep_data_list.append(tmp_dep)

class utilities:
    def get_num_data(self):
        return num_data_list

    def get_sym_data(self):
        return sym_data_list

    def get_dep_data(self):
        return dep_data_list

    def convert_data_list_to_dict(self, data_):
        tmp_dict = {}
        for x in range(0, len(data_[0])):
            tmp_dict[data_[0][x]] = []

        for i in range(1, len(data_)):
            for j, key in enumerate(tmp_dict.keys()):
                tmp_dict[key].append(data_[i][j])

        return tmp_dict

    #pp.pprint(get_num_data()[:10])
    #pp.pprint(get_sym_data()[:10])
    #pp.pprint(get_dep_data()[:10])

