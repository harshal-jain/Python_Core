# Function definition is here
def printinfo(*vartuple):
    "This prints a variable passed arguments"
    for var in vartuple:
        print(var)
    return


# Now you can call printinfo function
printinfo()
printinfo(454)
printinfo(70, 60, 50,"aa")