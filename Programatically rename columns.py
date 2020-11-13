# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import os

os.chdir(r'M:\01_Python\01a_StudentCourseSec')

os.getcwd()

stcraw ='Warehouse2020FA 1A STUDENT.COURSE.SEC V1.csv'

stc = pd.read_csv(stcraw, nrows=1)

names = stc.columns
namesclean = []

print(names)

for name in names:
    j = name.replace(' ','')
    k = j.replace('Stc','')
    namesclean.append(k)

print(names)
print(namesclean)

stccleancolumns = pd.read_csv(stcraw, names=namesclean)

stccleancolumns.columns

