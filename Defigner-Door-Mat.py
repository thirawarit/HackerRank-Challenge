# Enter your code here. Read input from STDIN. Print output to STDOUT
row, columm = map(int,input().split())   #Input a string and split it to a list.Put each str to int by map() and take it the variable.
for n in range(row//2) :      #Take loop n  by 0,1,2,...,int(row)
    print(('.|.'*(2*n+1)).center(columm,'-'))
print('WELCOME'.center(columm,'-'))
for n in range(row//2,0,-1) :    #Take reverse loop n by int(row), ..., 2, 1, 0
    print(('.|.'*(2*n-1)).center(columm,'-'))

#--------------------------------------------------------

print(' ')
pattern = [('.|.'*(2*n+1)).center(columm,'-') for n in range(row//2)]
print('\n'.join(pattern+['WELCOME'.center(columm,'-')]+pattern[::-1]))