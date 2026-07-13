total = 0
for i in range(5):
    price = float(input("Enter the price of ticket for person " + str(i+1) + ": "))
    total += price
print("Total price for 5 people is:", total)
