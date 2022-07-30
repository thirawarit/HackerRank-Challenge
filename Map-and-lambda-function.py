#Map and lambda function
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    box =[]
    for i in range(n) :
        if i != 0 and i != 1 :
            box.append(box[i-2]+box[i-1]) 
        else :
            box.append(i)
    return(box)
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))