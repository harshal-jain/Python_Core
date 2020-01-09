list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

"""
print ("list1[0]: ", list1[0]) #Offsets start at zero
print ("list2[1:5]: ", list2[1:5])  #Slicing fetches sections
print ("list1[-2]: ", list1[-2]) #Negative: count from the right


print ("Value available at index 2 : ", list1[2])
list1[2] = 2001
print ("New value available at index 2 : ", list1[2])


del list1[2]
print ("After deleting value at index 2 : ", list1)


print(list1+list2)
print(list1*3)
print(2000 in list1)
for x in [1,2,3] : print (x,end = ' ')



#Gives the total length of the list.
print (len(list1))


#Returns item from the list with max value. all data type should be same to calculate max
print (max(list2))


#Returns item from the list with min value. all data type should be same to calculate max
print (min(list2))

#The list() method takes sequence types and converts them to lists. This is used to convert a given tuple into list.
aTuple = (123, 'C++', 'Java', 'Python')
list3 = list(aTuple)
print ("List elements : ", list3)

str = "Hello World"

list4 = list(str)
print ("List elements : ", list4)

"""
#Python includes the following list methods −

#Appends object obj to list
list1.append('C#')
print(list1)


#Returns count of how many times obj occurs in list
a=list1.count('C#')
print(a)

#Appends the contents of seq to list
list1.extend(list2)
print(list1)

#Returns the lowest index in list that obj appears
print(list1.index('C#'))


#Inserts object obj into list at offset index
list1.insert(2, 'ASP')
print(list1)

#Removes and returns last object or obj from list
obj=list1.pop()
print(obj)
print(list1)

#Removes and returns last object or obj from list
obj=list1.pop(3)
print(obj)
print(list1)


#Removes object obj from list
list1.remove('C#')
print(list1)

#Reverses objects of list in place
list1.reverse()
print(list1)

#Sorts objects of list, use compare func if given
'''list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
'''

