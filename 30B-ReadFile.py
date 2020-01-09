

# Open a file
fo = open("foo.txt", "r")
str = fo.read(13)
print ("Read String is : ", str)

# Close opened file
fo.close()




# Open a file
fo = open("foo.txt", "r")
str = fo.read()
print ("Read String is : ", str)

# Close opened file
fo.close()