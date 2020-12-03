sample=int(input("please input the height :\n"))
if(sample>120):#avoid using {} becoz it does not allow multiline it only works for single line
        print("you can ride the coaster")
        age=int(input("input the age:\n"))
        if(age>=18):
            print("pleae pay $12")
            amount=12
        elif(age>=12):
            print("please pay $10")
            amount=10
        else:
            print("please $8")
            amount=8
        photo=input("want a photo on ticket :\n")
        if(photo=="yes"):
            amount+=3
            print(f"amount is :${amount}")
        else:
            print(f"amount is :${amount}")

else:

    print("you can't ride the coaster")
if(3==3 and 4==4):#and condition
    print("true")
    if (3 == 3 or 5 == 4):  # or condition
        print("true")
        a= not 2==3
        print(a)
