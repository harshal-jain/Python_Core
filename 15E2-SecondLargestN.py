n = input("how many numbers u want to take")
n = int(n)
lar = 0
slar=0;
for i in range(1, n + 1):
    no = input("Enter numer")
    no = int(no)

    if (no > lar):
        slar=lar
        lar = no
    elif (no > slar):
        slar = no


print(slar)

