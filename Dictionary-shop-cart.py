
'''
:::: Sample Input ::::

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

:::: Sample Output ::::

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

'''
num_item = int(input())
dict_shop = {}                                  #Dict for collection
for _ in range(num_item):
    item_name, space, price = input().rpartition(' ')        #split to list 2-3 values maybe...
    dict_shop.setdefault(item_name, 0) #setdefault if keyword is in the dict it will pass. 
    dict_shop[item_name] += int(price) #add value in keyword
'''
[NameDict].items() is one of dictionary methods, 
Returns a list containing a tuple for each key-value pair.
You can use this method and for-loop together to show both keywords and values.
'''
print("============================")
for x, y in dict_shop.items():
    print(x, y)                      