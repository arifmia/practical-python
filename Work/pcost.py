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

# Exercise 3.15: main() functions
# Main function
def main(argv):
    if len(sys.argv) == 2:
        #filename = sys.argv[1]
        cost = portfolio_cost(sys.argv[1])
        print('Total cost: ', cost)
    else:
        raise SystemExit('Usage: %s portfoliofile' % argv[0])
        #filename = 'data/portfolio.csv'
        #filename = 'data/portfoliodate.csv'

if __name__ == '__main__':    
    main(sys.argv)

