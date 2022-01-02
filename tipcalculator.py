numberOfSplits = int(input('How many people will you split the bill between: '))
bill = float(input('What is the bill total: '))
tip = int(input('How big of a % tip would you like to give: '))

# Calculate tip
TotalTip = (tip / 100) * bill

# Calculate bill plus the tip percentage
totalBill = bill + TotalTip

# Calculate how much each split will pay
pricePerSplit = totalBill / numberOfSplits

# print answer to user
print(f'Each person should pay: {pricePerSplit:.2f}')