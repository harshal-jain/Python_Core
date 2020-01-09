str="Jai Shri Ram Shri"
#Capitalizes first letter of string
print(str.capitalize());

#Returns a string padded with fillchar with the original string centered to a total of width columns.
print(str.center(30,'a'));

#The count() method returns the number of occurrences of substring sub in the range [start, end].
print(str.count('ri'));
print(str.count('ri',7,17));

#The expandtabs() method returns a copy of the string in which the tab characters ie. '\t' are expanded using spaces, optionally using the given tabsize
str = "this is\tstring example....wow!!!"
print ("Original string: " + str)
print("\r")

print ("Double exapanded tab: " +  str.expandtabs(16))
print("\r")

# initializing string
str = "i\tlove\tCars"
# using expandtabs to insert spacing
print("Modified string using default spacing: ", end="")
print(str.expandtabs())

print("\r")

# using expandtabs to insert spacing
print("Modified string using less spacing: ", end="")
print(str.expandtabs(2))

print("\r")

# using expandtabs to insert spacing
print("Modified string using more spacing: ", end="")
print(str.expandtabs(12))

print("\r")
