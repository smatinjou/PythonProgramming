def isprime(n):
    
    if n==1 or n<0:
        return 0
    elif n==2:
        return 1
    else:
        c=[]
        for i in range(2,n):
            if n%i==0:
                c.append(i)
        if len(c)==0:
            return 1
        else:
            return 0

print("exit=0")
while True:
    n=int(input("please enter a number = "))
    if n==0:
        break
    print(bool(isprime(n)))
