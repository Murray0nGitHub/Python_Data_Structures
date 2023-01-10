#You are analyzing house prices. The given code declares a list with house prices in the neighborhood.
#You need to calculate and output the number of houses that have a price that is above the average.

#To calculate the average price of the houses, you need to divide the sum of all prices by the number of houses.
#Use sum(list) to calculate the sum of all items in the list and len(list) to get the number of items.

prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

avg = sum(prices)/len(prices)
count = 0
for i in prices:
    if i > avg:
        count +=1
print(count)