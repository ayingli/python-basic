import csv

filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    #print(header_row)

