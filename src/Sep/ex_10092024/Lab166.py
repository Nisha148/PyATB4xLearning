import csv

with open("Testdata.csv") as csvfile:
    reading=csv.reader(csvfile)
    for col in reading:
        print(col[0],col[1],sep="|")