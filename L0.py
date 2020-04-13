import csv
with open('location.csv') as csv_file:
    rows = csv.reader(csv_file)
    for row in rows:
        print(row)