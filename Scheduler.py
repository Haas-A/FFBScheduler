import csv

filename = 'FourDiv.csv'

file = open(filename, 'r')

data = csv.DictReader(file)

numDivs = len(data.fieldnames)

Divs = {}
for row in data:
    for i in range(1, numDivs):
        print(i)
        print(row[str(i)])

print(data.fieldnames)