'''
==== Constraints ====
All coefficients of polynomial P are integers. 
x and y are also integers.

==== Sample Input ====
1 4
x**3 + x**2 + x + 1
==== Sample Output ====
True

'''
# The eval() function evaluates the specified expression, ...
# if the expression is a legal Python statement, it will be executed.

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, result = map(int, input().split())
polynomial = input()
print(eval(polynomial) == result)
