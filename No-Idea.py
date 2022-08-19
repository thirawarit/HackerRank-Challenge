'''
Input Format
The first line contains integers M and N separated by a space. 
The second line contains M integers, the elements of the array. 
The third and fourth lines contain N integers, A and B, respectively.
Output Format
Output a single integer, your total happiness.
Sample Input
3 2
1 5 3
3 1
5 7
Sample Output
1
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
size_arr, size_set = map(int, input().split())
arr = input().split() #the array might contain duplicate elements.
set_a = set(input().split())
set_b = set(input().split())
happ = 0
for i in arr:
    if i in set_a:
        happ += 1
    elif i in set_b:
        happ -= 1
print(happ)
