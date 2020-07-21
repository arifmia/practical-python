# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            #print(record)
            try:
                stock = {
                    'name'   : record['name'],
                    'shares' : int(record['shares']),
                    'price'   : float(record['price'])
                }
                portfolio.append(stock)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def create_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        price = prices[stock['name']]
        change = price - stock['price']
        summary = (stock['name'], stock['shares'], price, change)
        rows.append(summary)
    return rows

if len(sys.argv) == 3:
    filePortfolio = sys.argv[1]
    filePrices = sys.argv[2]
else:
    filePortfolio = 'data/portfoliodate.csv'
    filePrices = 'data/prices.csv'

# Call Read data files function here
portfolio = read_portfolio(filePortfolio)
prices = read_prices(filePrices)
#pprint(portfolio)
#pprint(prices)
# Create report
report = create_report(portfolio, prices)
#report output
headers = ('Name', 'Shares', 'Price', 'Change')
#print(headers)
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    #print("%10s %10d %10.2f %10.2f" % row)
    print('%10s %10d %10.2f %10.2f' %row)