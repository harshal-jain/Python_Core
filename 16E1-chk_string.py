n=input("Enter Number ");

flag=0;
for val in n:
    code=ord(val);
    if not(code >= 48 and code <=57):
        flag=1;
        break;

if(flag==1):
    print("invalid")
else:
    print("Valid")
