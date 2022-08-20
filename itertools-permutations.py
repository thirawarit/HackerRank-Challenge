'''
====Output Format====
Print the permutations of the string S on separate lines.

====Sample Input====
HACK 2

====Sample Output====
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations as permut
string, r = input().split()
permut_string = sorted(list(permut(string, int(r))))
#sort() changes the list directly and doesn't return any value
#If we want to return the sorted list you should to use sorted(list,..)
#in the other hands, the list doesn't change too.
for i in permut_string:
    print(''.join(i))