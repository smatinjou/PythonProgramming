import math
##y=ax**2+bx+c

def equation2D(a,b,c):
    def getDelta():
        return b**2-4*a*c
    delta=getDelta()
    if delta<0:
        return None
    elif delta==0:
        x1=-b/(2*a)

        return x1
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return (x1,x2)
#example:
print(equation2D(1,0,-1)) #x**2-1   ,   x1=1 x2=-1
print(equation2D(1,-2,1)) #x**2-2x+1    ,   x1=1 x2=1
print(equation2D(1,0,1))  #x**2+1   no roots

print("################")

a=int(input("please enter a from y=ax**2+bx+c  ==> a= "))
b=int(input("please enter b from y=ax**2+bx+c  ==> b= "))
c=int(input("please enter c from y=ax**2+bx+c  ==> c= "))
print(equation2D(a,b,c))

