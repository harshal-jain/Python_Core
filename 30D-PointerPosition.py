# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
# seek(character position , file position 0= beginning of the file and 1 =current position and 2 =end of the file
position = fo.seek(20, 0)
str = fo.read(10)
print ("Again read String is : ", str)

# Close opened file
fo.close()