# Enter your code here. Read input from STDIN. Print output to STDOUT
num_element, element = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    temp_contain, temp_num = input().split()
    if temp_contain == 'update':
        element.update(map(int, input().split()))
    elif temp_contain == 'intersection_update':
        element.intersection_update(map(int, input().split()))
    elif temp_contain == 'symmetric_difference_update':
        element.symmetric_difference_update(map(int, input().split()))
    elif temp_contain == 'difference_update':
        element.difference_update(map(int, input().split()))
    else:
        print('error from messages in an algorithm!!')
print(sum(element))
