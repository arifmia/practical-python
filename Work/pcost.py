# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    totalcost = 0.0
    with open(filename, 'rt') as file:
        next(file)
        for line in file:
            #print(line.split(',')[1])        
            totalcost += int(line.split(',')[1]) * float(line.split(',')[2])
    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)
