# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint
import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def create_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        price = prices[stock['name']]
        change = price - stock['price']
        summary = (stock['name'], stock['shares'], price, change)
        rows.append(summary)
    return rows

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    #print(headers)
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        #print("%10s %10d %10.2f %10.2f" % row)
        print('%10s %10d %10.2f %10.2f' %row)

def portfolio_report(filePortfolio, filePrices):
    # Call Read data files function here
    portfolio = read_portfolio(filePortfolio)
    prices = read_prices(filePrices)
    # Create report
    report = create_report(portfolio, prices)
    # Call custome report print function
    print_report(report)

if len(sys.argv) == 3:
    filePortfolio = sys.argv[1]
    filePrices = sys.argv[2]
else:
    filePortfolio = 'data/portfolio.csv'
    filePrices = 'data/prices.csv'

# Exercise 3.12: Using your library module
# Call this single function to produce the report
portfolio_report(filePortfolio, filePrices)