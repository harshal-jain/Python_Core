n = int(input("Show the multiplication upto ?  "))

for i in range(1, n+1):
    for no in range(1, 11):
        print(i, 'x', no, '=', no * i)
    print("");
