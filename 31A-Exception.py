"""

try:
    # Open a file
    fo = open("foo.txt", "w")
    fo.write("Python is a great language.\nYeah its great!!\n")


except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   # Close opend file
   fo.close()

"""


try:
    # Open a file
    fo = open("foo1.txt", "r")
    str = fo.read()
    print("Read String is : ", str)

    # Close opened file
    fo.close()

except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("read content from file successfully")