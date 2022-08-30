#sale by match
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
'''
Sample Input
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
vvvvvvvvvvvvvvvvvvv
9
10 20 20 10 10 30 50 10 20
^^^^^^^^^^^^^^^^^^^
Sample Output
3

'''

def sockMerchant(n, ar):
    # Write your code here
    #==========My Solution=============
    '''
    from collections import Counter
    count = 0
    socket = Counter(ar)
    for i in set(ar):
        if socket[i]%2 == 1:
            count += (socket[i] - 1)//2
        else:
            count += socket[i]//2
    return(count)
    '''
    #==========Other Solution==========
    ar.sort()       #[10,10,10,10,20,20,20,30,50]
    temp = 0        #attribute for tracking
    pair = 0        #attribute for count
    for x in ar:            #get each item 
        if x == temp:       #ex. x = 10 : 10 == 0 FALSE
            pair += 1       #
            temp = 0        #
        else:               #
            temp = x        #temp = 10
    return(pair)

            
        

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
