dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


#print ("dict['Alice']: ", dict['Alice'])
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


#del dict['Name'] # remove entry with key 'Name'
#dict.clear()     # remove all entries in dict
#del dict         # delete entire dictionary


dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print ("New Dictionary : ",dict2)


dict2.clear()
print ("New Dictionary : ",dict2)

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict))
