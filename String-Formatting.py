def print_formatted(number):
    # your code goes here
    
    space = len('{:b}'.format(number))
    
    for i in range(number) :
        i+=1
        decimal = '{:d}'.format(i).rjust(space,' ')
        octal = '{:o}'.format(i).rjust(space,' ')
        Hexadecimal = '{:X}'.format(i).rjust(space,' ')
        binary = '{:b}'.format(i).rjust(space,' ')
        print(decimal,octal,Hexadecimal,binary)

        
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)