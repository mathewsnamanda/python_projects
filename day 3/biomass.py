weight = input("enter the mass of the body in kg \n")
height = input("input the height in m \n")
BMI = int(weight)/(float(height)**2)#raised to power with normal division returning a float
BMI1=int(weight)//(float(height)**2)#flow division returns always integer
print("the BMI is: ")
print(round(BMI,2))
print(BMI1)
result=2
result/=2#it is dividing result by 2 instead of overwriting itself
print(result)
score=0
weight=1.56
married=True
print(f"your score is {score}"+f" your weight is: {weight}" +f" and married status is : {married}")#f-string allows combinations of different variables