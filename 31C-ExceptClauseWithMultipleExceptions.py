try:
    # Open a file
    fo = open("foo1.txt", "r")
    str = fo.read()
    print("Read String is : ", str)

    # Close opened file
    fo.close()

except (IOError, RuntimeError):
   print ("Error: can\'t find file or read data")
else:
   print ("read content from file successfully")