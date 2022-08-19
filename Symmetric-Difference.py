'''
Sample Input
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output
5
9
11
12
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_a = int(input())
a = set(map(int, input().split(' ', num_a)))
num_b = int(input())
b = set(map(int, input().split(' ', num_b)))
a.symmetric_difference_update(b)
box = list(a)
box.sort()
for i in box:
    print(i)
