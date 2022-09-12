import csv
import pprint as pp
from webbrowser import get

# Read csv file with a comma as the delimiter, then split the data according
# to num, sy and dependent data
csvfile = open('hw2test.csv', 'r')
datalist = []
for row in csv.reader(csvfile, delimiter=","):
    datalist.append(row)

numcols = []
numdict = {}
symcols = []
symdict = {}
depcols = []
depdict = {}

# split the data according to num and sym definitions
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

# utilities class which holds functions go get data as a 2D list and 
# another function to convert the 2D list data into a dictionary format.
class utilities:

    # get num data as a 2D array
    def get_num_data(self):
        return num_data_list

    # get sym data as a 2D array
    def get_sym_data(self):
        return sym_data_list

    # get dependent data as a 2D array
    def get_dep_data(self):
        return dep_data_list

    # convert 2D array data into a dictionary
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

