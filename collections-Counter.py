#collections.Counter()
'''
collections.Counter() 
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
=================================
Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200

Explanation
Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num_shoe = int(input())
list_shoe = Counter(map(int,input().split()))
price = 0 
for _ in range(int(input())):
    size_patron, price4shoe = list(map(int, input().split()))
    if list_shoe[size_patron] != 0: 
        list_shoe[size_patron] -= 1
        price += price4shoe
print(price)
    
    
    