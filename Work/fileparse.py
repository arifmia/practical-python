# fileparse.py
#
# Exercise 3.3
import sys
import csv
import gzip

# Exercise 3.18: Fixing existing functions
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''       
    rows = csv.reader(filename, delimiter=delimiter)
    
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
    for rowno, row in enumerate(rows, 1):
        if not row:    # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [ row[index] for index in indices ]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary
        if has_headers:
            record = dict(zip(headers, row))
            records.append(record)
        else:
            records.append(row)

    return records