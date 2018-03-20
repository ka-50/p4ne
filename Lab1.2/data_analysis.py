#!/usr/local/bin/phython3
import sys
from matplotlib  import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
def getvalue(x): return x.value

print(list(map(getvalue, sheet['A'][1:5])))

years = list(map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
act = list(map(getvalue, sheet['D'][1:]))
#pyplot.plot(years, temp, label="Y\T")
#pyplot.plot(years, act, label="Y\A")

pyplot.show()

