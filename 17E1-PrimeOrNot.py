# start=int(input("Enter the number"))
# end=int(input("Enter the number"))
#
# for n in range(start,end+1,1):
#     n=int(n)
#     for i in range(2,n):
#         if(n%i==0):
#             #print("not prime")
#             break
#     else:
#         print(str(n)+"prime")
#
#



start=int(input("Enter the number"))
end=int(input("Enter the number"))

for n in range(start,end+1,1):
    n=int(n)
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break

    if(flag==0):
        print(n)


