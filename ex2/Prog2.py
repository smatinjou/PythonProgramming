import random

x=int(input("enter x number ---> x = "))
y=int(input("enter x number ---> y = "))

if x%2==0:
    x+=1

z=[]
h=(y-x)/2
while len(z)<=h-1:
    i=random.randrange(x,y)
    if i%2==0 and i not in z:
        z.append(i)
        
print(z)


    
