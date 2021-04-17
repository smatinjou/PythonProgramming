import random

x=int(input("please enter min = "))
y=int(input("please enter max = "))

while True:
    a=random.randrange(x,y)
    if a%2==0:
        print(a)
        break
