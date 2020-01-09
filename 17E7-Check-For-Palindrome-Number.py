n= input("enter the number");
p= len(n)-1;
n=int(n);
temp=n
reverse = 0



while n>0:
    rem=n%10;
    reverse= reverse+ rem*(10**p);
    n=n//10;
    p=p-1;

print("reversed number is", reverse);

if(temp==reverse):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
