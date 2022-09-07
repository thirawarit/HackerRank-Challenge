#Merge-the-tools.py
'''
============
Function Description
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:
string s    : the string to analyze
int k       : the size of substrings to analyze
============
Prints
Print each subsequence on a new line. There will be  of them. No return value is expected.
============
Input Format
The first line contains a single string, s. 
The second line contains an integer, k, the length of each substring.
============
Sample Input
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
vvvvvvvvvvvvv
AABCAAADA
3
===============
Sample Output
AB
CA
AD
'''

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        package = []
        for j in list(string[i:i+k]):
            if not j in package:
                package.append(j)
        print(''.join(package))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)