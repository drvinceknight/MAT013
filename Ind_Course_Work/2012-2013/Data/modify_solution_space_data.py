#!/usr/bin/env python

from sys import argv
import csv

f = open(argv[1], "rb")
data = csv.reader(f)
data = [[row[0], row[1], row[2], row[6], row[7], row[8]] for row in data]
f.close()

f = open("Solution_Space_Exploration.csv", "wb")
outfile = csv.writer(f)

for row in data:
    outfile.writerow(row)

f.close()
