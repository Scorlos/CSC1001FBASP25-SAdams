# Snack Bar Lab

def totalCalc (num1, num2, num3, num4):
    return (.50 * num1) + (1.00 * num2) + (.25 * num3) + (.75 * num4)

bottlesWater = int(input("How many bottles of water were purchased? "))
candyBars = int(input("How many candy bars were purchased? "))
popcornBags = int(input("How many bags of popcorn were purchased? "))
cansSoda = int(input("How many candy bars were purchased? "))
totalCost = totalCalc(bottlesWater, candyBars, popcornBags, cansSoda)
print("The total cost is" , totalCost)