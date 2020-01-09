a=input("Enter the first number,a=")
b=input("Enter the Second number,b=")
c=input("Enter the Third number,c=")
if(a>b):
    if(a>c):
        print(str(a)+" is Maximum Number")
    else:
        print(str(c)+ " is Maximum Number")

else:
    if(b>c):
        print(str(b)+" is Maximum Number")
    else:
        print(str(c)+" is Maximum Number")

