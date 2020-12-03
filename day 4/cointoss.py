import random
seed=int(input("input seed number:\n"))
random.seed(seed)
randominteger=random.randint(1,10)
print(f"sample seed value: {randominteger}")
randomfloat=random.random()*5
print(randomfloat)

