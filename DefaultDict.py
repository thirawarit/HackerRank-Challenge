'''
==== INPUT ====
10 3    group A size n = 10, group B size m = 3
a       group A contains ...
a
b
a
b
b
a
a
b
a
a       group B contains 'a', 'b', 'c'
b
c
================
10 3 
a
a
b
a
b
b
a
a
b
a
a
b
c
==== OUTPUT ====
1 2 4 7 8 10
3 5 6 9
-1
=================
In the sample problem, if 'c' also appeared in word group B, you would print 'c'.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
size_a, size_b = map(int,input().split())
result = defaultdict(list)  #{_:[...], _:[...]}
for i in range(1,size_a+1):
    result[input()].append(i)  #{a:[1, 3, ...], b:[2, 4, ...]}
for _ in range(size_b):
    box = input()
    print(*result[box]) if box in result else print(-1)