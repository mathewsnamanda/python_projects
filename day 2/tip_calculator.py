print("welcome to the tip calculator")
bill=float(input("what was the total bill? $"))
percentage=float(input("whats is the percentage tip you would like to give it? 10  15  20"))
people=float(input("how many people would like to split it to: "))
paid=(bill*((percentage/100)+1))/people
paid1=round(paid,3)#if floating remember to add one excess decimal but if integer just enter exact decimal
print(f"each person would pay: {paid1} dollars")