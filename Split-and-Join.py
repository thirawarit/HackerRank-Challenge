
def split_and_join(line) :
    #Writen your code here.
    Split = line.split()    #Func 'string'.split() must have a variable to get a list.
    Join = '-'.join(Split)  #Func 'string'.join() must have a variable to get a new string.
    return(Join)
if __name__ == '__main__' :
    line = input()
    result = split_and_join(line)
    print(result)