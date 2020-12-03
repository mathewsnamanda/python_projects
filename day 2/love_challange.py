name=input("enter your name :\n").lower();#casting to lower case or upper case function
hername=input("enter your partner name: \n")
name+=hername
l=name.count("l")#counting no of letters in a word
l+=name.count("o")
l+=name.count("v")
l+=name.count("e")
l+=name.count("t")
l+=name.count("r")
l+=name.count("u")
l+=name.count("e")
print(f"the score is: {l}")
print('you\"\'re lovely')#having a backtik converts the speech mark into string/interprets it as string