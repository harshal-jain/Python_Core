# a=0b1011
# b=0b1000
# print(a&b)
# print(bin(a&b)) #Binary AND
# print(bin(a|b)) #Binary OR
# print(a^b)      # XOR
# print(bin(a^b)) #Binary AND
# print(bin(~a))  #Binary Ones Complement
# print(bin(a<<2)) #Binary Left Shift
# print(bin(a<<4))
# print(bin(a>>2)) #Binary Right Shift
# print(bin(a>>4))
#



a = 10            # 10 = 0000 1010
b = 5            # 5   = 0000 0101
c = 0

c = a & b;        # 0 = 0000 0000
print ("Line 1 - Value of c is ", c)

c = a | b;        # 15 = 0000 1111
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 15 = 0000 1111
print ("Line 3 - Value of c is ", c)

c = ~a;           # -11 =  0000 1101
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 00 101000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 000000 10
print ("Line 6 - Value of c is ", c)









