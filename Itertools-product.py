'''

Sample Input
 1 2
 3 4
 ==================
Sample Output
 (1, 3) (1, 4) (2, 3) (2, 4)
 
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

#print(*product(a, b))

def product_self(a, b):
    c=[]
    for i in a:
        for j in b:
            c.append((i, j))
    return(' '.join(map(str, c)))
    
print(product_self(a,b))

