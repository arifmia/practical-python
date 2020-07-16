# bounce.py
#
# Exercise 1.5
height = 100
bounces = 0
distance = height
while bounces < 10:
    height *= (3/5)
    print(bounces + 1, round(height, 4))    
    bounces += 1
