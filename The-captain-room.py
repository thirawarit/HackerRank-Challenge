# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output
8
'''
K = int(input())
ele_group = list(map(int, input().split()))
d = dict()
for a in set(ele_group):
    d.setdefault(a, 0)
for x in ele_group:
    d[x] += 1
for i, j in d.items():
    if j != K:
        print(i)

'''
######################################
#The pattern of coding about counting#
K = 5
unordered_ele = [map(int, '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3                 6 8 4 3 1 5 6 2 '.split())]
dict_box = {}
for i in unordered_ele:
    dict_box[i] = 1 + dict_box.get(x, 0)
for x, y in dict_box.items():
    if y != K:
        print(x)
    
'''