item = [1,2,3,4,5,6]
*check, box, cat = ['a', 'b', 'c', 'd']
item_map = [*map(str, item)]
item_map2 = list(map(str, item))
print(item_map, item_map2, *item_map2, check, box, sep='\n')
