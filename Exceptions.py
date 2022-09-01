#Exceptions
'''
Task
You are given two values a and b. 
Perform integer division and print a/b.
====================
Input Format
The first line contains T, the number of test cases. 
The next T lines each contain the space separated values of a and b.
====================
Constraints
0 < T < 10
====================
Output Format
Print the value of a/b. 
In the case of ZeroDivisionError or ValueError, print the error code.
====================
Sample Input
3
1 0
2 $
3 1 
====================
Sample Output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
====================
Note: 
For integer division in Python 3 use //.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as zd:
        print('Error Code: {}'.format(zd))
    except ValueError as ve:
        print("Error Code: {}".format(ve))
#get exception with 'as' and 'format'
