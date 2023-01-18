import csv

with open('data/1117.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
