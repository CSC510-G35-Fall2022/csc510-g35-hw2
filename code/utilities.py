import csv
import pprint as pp


csvfile = open('hw2test.csv', 'r')
datalist = []
for row in csv.reader(csvfile, delimiter=","):
    datalist.append(row)

numcols = []
numdict = {}
symcols = []
symdict = {}

ct = 0
for i in datalist[0]:
    if i[0].isupper() and i[-1] != '+' and i[-1] != '-' and i[-1] != ':':
        numcols.append(i)
        numdict[i] = ct
    if  i[-1] == '-' or i[-1] == '+':
        symcols.append(i)
        symdict[i] = ct
    ct += 1


num_data_list = []
sym_data_list = []

for idx in range (0, len(datalist)):
    tmp_num = []
    tmp_sym = []
    for x in range (0, len(datalist[idx])):
        if x in list(numdict.values()):
            tmp_num.append(datalist[idx][x])
        if x in list(symdict.values()):
            tmp_sym.append(datalist[idx][x])
    
    num_data_list.append(tmp_num)
    sym_data_list.append(tmp_sym)

class utilities:
    def get_num_data():
        return num_data_list

    def get_sym_data():
        return sym_data_list

    pp.pprint(get_num_data())
    pp.pprint(get_sym_data())

