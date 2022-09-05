import csv
import statistics
csvfile= open('hw2test.csv','r')
datalist=[]
for row in csv.reader(csvfile,delimiter=","):
    datalist.append(row)
numcols=[]
numdict={}
symcols=[]
symdict={}
ct=0
for i in datalist[0]:
    if i[0].isupper() and i[-1]!=':':
        numcols.append(i)
        numdict[i]=ct
        ct+=1
    elif i[0].islower() and i[-1]!=':':
        numcols.append(i)
        symdict[i]=ct
        ct+=1