n=int(input("enter a number = "))
c=[]
for i in range(1,n+1):
    if n%i==0:
        c.append(i)
print(n,"maghsum elayhs --->",c)
