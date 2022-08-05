# Enter your code here. Read input from STDIN. Print output to STDOUT
row, columm = input().split()   #Input a string and split it to a list.Put each string to the variable.
for n in range((int(row))//2) :      #Take loop n  by 0,1,2,...,int(row)
    print(('.|.'*(2*n+1)).center(int(columm),'-'))
print('WELCOME'.center(int(columm),'-'))
for n in range((int(row))//2,0,-1) :    #Take reverse loop n by int(row), ..., 2, 1, 0
    print(('.|.'*(2*n-1)).center(int(columm),'-'))