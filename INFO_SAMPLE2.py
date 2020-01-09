str=input("Enter the string")
l=len(str)
lst=""
lst=list(lst)
for i in range(0,l):
    c1=str[i]
    for j in range(i+1,l):
        c2=str[j]
        if(c1!=c2):
            cch=c1+c2
            len_cch=len(cch)
            for i in range(0,l):
                for j in range(i+1,l):

                    if(lst[i]==lst[j]):
                        break

            lst.append(cch)
            #print(cch)



print(lst)