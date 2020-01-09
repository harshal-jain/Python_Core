n=input("how many numbers u want to take")
n=int(n)
lar=0
for i in range(1,n+1):
    no=input("Enter numer")
    no=int(no)

    if(no>lar):
        lar=no


print(lar)
