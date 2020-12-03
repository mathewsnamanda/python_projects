import random
fruit=["sample","two"]
fruit2=["spp2","spp4","spp99"]
fruit.append("sample2")#appending adds string to an array
fruit.extend(fruit2) #extending adds a list to existing list
fruit.insert(0,"sample9090")#inserting a value between a given position in an array
fruit.remove("sample")#removes a given string
string2="hello,mr,namanda"
op=string2.split(",")#it is used to split string by simple inside the bracket
fruit.extend(op)
length=len(fruit)
randio=random.randint(0,length)
print(fruit[int(randio)])
randomchoice=random.choice(fruit)
print(randomchoice)#random choices using random function

array1=["one","two","three"]
array2=["ten","twenty","thirty"]
array3=[array1,array2]
print(array3[1])
