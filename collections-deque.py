#collections-deque.py
'''
Task
Perform append, pop, popleft and appendleft methods on an empty deque d.
Input Format
The first line contains an integer N, the number of operations. 
The next N lines contains the space separated names of methods and their values.
=============================
Constraints
0 < N <= 100
=============================
Output Format
Print the space separated elements of deque d.
=============================
Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft
=============================
Sample Output
1 2
'''
from collections import deque
ele_deque = deque()
for _ in range(int(input())):
    methods, space, items = input().partition(' ')
    if methods in ['clear', 'pop', 'popleft', 'reverse']:
        command = 'ele_deque.{}()'.format(methods)
        eval(command)
    else:
        command = 'ele_deque.{}(items)'.format(methods)
        eval(command)
print(*ele_deque)
