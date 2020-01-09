p=2
rev=0;
n=int(input("enter the number"));
while n>0:
   rem= n%10;
   rev=rev+rem*(10**p);
   n= n//10;
   p=p-1;
print ("reverse number is", rev);
