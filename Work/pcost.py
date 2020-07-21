# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    totalcost = 0.0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        #for line in file:
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            print(record)
            #totalcost += int(line.split(',')[1]) * float(line.split(',')[2])
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                totalcost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    #filename = 'data/portfolio.csv'
    filename = 'data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)
