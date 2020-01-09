# Function definition is here
"""
def changeme(mylist):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", mylist)

    mylist[2] = 50
    print("Values inside the function after change: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

"""

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This would assi new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


