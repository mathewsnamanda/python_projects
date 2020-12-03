age=input("enter your age in years:\n")#all inputs is usually floats therefore casting is required
years=90-int(age)
months=years*12
weeks=52*years
days=365*years
print(f"you have got {months} months,{weeks} weeks and {days} days \n")