#!/usr/bin/env python

import csv

f = open("Shut_the_Box.csv", "rb")
data = csv.reader(f)
data = [row for row in data]
f.close()

f = open("Greedy.csv", "wb")
outfile = csv.writer(f)
outfile.writerows([["Score", "Length"]])
f.close()
f = open("Random.csv", "wb")
outfile = csv.writer(f)
outfile.writerows([["Score", "Length"]])
f.close()
f = open("Longest.csv", "wb")
outfile = csv.writer(f)
outfile.writerows([["Score", "Length"]])
f.close()
f = open("Shortest.csv", "wb")
outfile = csv.writer(f)
outfile.writerows([["Score", "Length"]])
f.close()

for row in data[1:]:
    f = open("Greedy.csv", "a")
    outfile = csv.writer(f)
    outfile.writerow([row[0], len(eval(row[1]))])
    f.close()
    f = open("Random.csv", "a")
    outfile = csv.writer(f)
    outfile.writerow([row[2], len(eval(row[3]))])
    f.close()
    f = open("Longest.csv", "a")
    outfile = csv.writer(f)
    outfile.writerow([row[4], len(eval(row[5]))])
    f.close()
    f = open("Shortest.csv", "a")
    outfile = csv.writer(f)
    outfile.writerow([row[6], len(eval(row[7]))])
    f.close()
