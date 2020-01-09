a=input("Enter the first number");
b=input("Enter the second number");
a=int(a)
b=int(b)
print("before swapping a="+str(a)+",b="+str(b) )

a=a+b
b=a-b
a=a-b


print("after swapping a="+str(a)+",b="+str(b) )

