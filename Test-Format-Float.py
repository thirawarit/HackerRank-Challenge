import math
x = 100.12345
format_f = '{0:.3g}'.format(x)  
# str.format(), str is '{0:.3g}' 
# It will display 3 number, counted on all number from left to right
# answer : 100
print(format_f)
print(" ")
f2_format = '{0:.2f}'.format(x) 
# str.format(), str is '{0:.3f}'
# It will format the float with 2 decimal places.
# answer : 100.12
print(f2_format)
print(" ")
print("answer trucate is ",math.trunc(x))
# The truncate value is the floating-point numbers that remove decimal parts.
# answer : 100
print(" ")
print("answer ceil is ",math.ceil(x))
# The ceil value is the smallest integer greater than the number.
# answer : 101
