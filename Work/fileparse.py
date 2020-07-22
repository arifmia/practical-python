# fileparse.py
#
# Exercise 3.3
import sys
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records

if len(sys.argv) == 2:
    csvfilepath = sys.argv[1]
else:
    csvfilepath = 'data/portfolio.csv'

read_csv = parse_csv(csvfilepath)
print(read_csv)