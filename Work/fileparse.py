# fileparse.py
#
# Exercise 3.3
import sys
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
#def parse_csv(filename, select=None, types=None, has_headers=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
       
        # Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]
            if types:
                row = [func(val) for func, val in zip(types, row) ]

            # Make a dictionary
            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            else:
                records.append(row)

    return records

if len(sys.argv) == 2:
    csvfilepath = sys.argv[1]
else:
    csvfilepath = 'data/prices.csv'
# Exercise 3.8: Raising exceptions
try:
    read_csv = parse_csv(csvfilepath, select=['name','price'], has_headers=False)
except (IOError,LookupError,RuntimeError) as e:    
    raise RuntimeError    
#read_csv = parse_csv(csvfilepath, types=[str, int, float], has_headers=True, delimiter=' ')

print(read_csv)