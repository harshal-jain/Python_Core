import operator

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
print ("tup2[2:]: ", tup2[2:])
print ("tup2[:2]: ", tup2[:2])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)


tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
# del tup;
print ("After deleting tup : ")
print (tup)


print(len(tup))
print(tup*3)
print(1997 in tup)


for x in (1,2,3) : print (x, end = ' ')


## functions
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print(len(tup1))
print(max(tup2))
print(min(tup2))

list1 = ['maths', 'che', 'phy', 'bio']
tuple1 = tuple(list1)
print ("tuple elements : ", tuple1)


