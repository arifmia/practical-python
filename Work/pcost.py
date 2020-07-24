# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    totalcost = 0.0
    portfolio = report.read_portfolio(filename)
    for rowno, row in enumerate(portfolio, start=1):
            #record = dict(zip(headers, row))
            #print(record)
            #totalcost += int(line.split(',')[1]) * float(line.split(',')[2])
            try:
                nshares = int(row['shares'])
                price = float(row['price'])
                totalcost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'
    #filename = 'data/portfoliodate.csv'

# Exercise 3.14: Using more library imports
cost = portfolio_cost(filename)
print('Total cost: ', cost)
