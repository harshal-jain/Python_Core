import math

# The absolute value of x: the (positive) distance between x and zero.
print(abs(5.5));

# The absolute value of x.
print(math.fabs(-5.5))

# The exponential of x: ex
print(math.exp(5))

# The ceiling of x: the smallest integer not less than x.
print(math.ceil(4.1));
print(math.ceil(4.49));
print(math.ceil(4.5));
print(math.ceil(4.99));

# The floor of x: the largest integer not greater than x.
print(math.floor(4.1));
print(math.floor(4.49));
print(math.floor(4.5));
print(math.floor(4.99));

# x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
print(round(4.1));
print(round(4.49));
print(round(4.5));
print(round(4.99));

# The natural logarithm of x, for x > 0.
print(math.log(5))

# The base-10 logarithm of x for x > 0.
print(math.log10(5))

# The largest of its arguments: the value closest to positive infinity
print(max(5, 6, 7))

# The smallest of its arguments: the value closest to negative infinity.
print(min(5, 6, 7))

# The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.
print(math.modf(5.9))

# The value of x**y.
print(pow(3, 3))

# The square root of x for x > 0.
print(math.sqrt(9))
