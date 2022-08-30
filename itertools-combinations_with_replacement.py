#itertools-combinations_with_replacement.py
'''
Task
    You are given a string S. 
    Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
===============
Input Format
    A single line containing the string S and integer value k separated by a space.
===============
Constraints
     0 < k <= len(S)
    The string contains only UPPERCASE characters.
===============
Output Format
    Print the different combinations of string S on separate lines.
================
Sample Input
HACK 2
================
Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as comb_w_rep
string, n = input().split()
box = list(comb_w_rep(sorted(string), int(n)))
for i in box:
    print(''.join(i))