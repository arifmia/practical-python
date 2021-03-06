# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint
import fileparse

def read_portfolio(filename):
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,types=[str,float], has_headers=False))

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
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:        
        print('%10s %10d %10.2f %10.2f' %row)

def portfolio_report(filePortfolio, filePrices):
    # Call Read data files function here
    portfolio = read_portfolio(filePortfolio)
    prices = read_prices(filePrices)
    # Create report
    report = create_report(portfolio, prices)
    # Call custome report print function
    print_report(report)

# Exercise 3.18: Fixing existing functions
# Main function
def main(argv):
    # Parse command line args, environment, etc.   
    if len(sys.argv) == 3:        
        portfolio_report(sys.argv[1], sys.argv[2])
    else:
        raise SystemExit('Usage: %s portfoliofile pricefile' % argv[0])        

if __name__ == '__main__':    
    main(sys.argv)
