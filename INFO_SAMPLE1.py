Andrea_Total=int(input(""))
lst_a=""
for i in range(1,Andrea_Total+1):
    lst_a= lst_a + input("")

lst1 = list(lst_a)




Maria_Total=int(input(""))
lst_b=""
for i in range(1,Andrea_Total+1):
    lst_b= lst_b + input("")

lst2 = list(lst_b)



E_O=input("")
if(E_O=="even" or E_O=="Even"):
    total_A = 0
    for i in range(0,len(lst1),2):
        total_A=total_A+(int(lst1[i])-int(lst2[i]))


    total_A_o = 0
    for i in range(0, len(lst1),2 ):
        total_A_o=total_A_o+(int(lst2[i])-int(lst2[i]))

else:
    total_A = 0
    for i in range(1, len(lst1), 2):
        total_A = total_A + (int(lst1[i]) - int(lst2[i]))

    total_A_o = 0
    for i in range(1, len(lst1), 2):
        total_A_o = total_A_o + (int(lst2[i]) - int(lst2[i]))



if(total_A_o>total_A):
    print("MARIA")
else:
    print("ANDREA")









