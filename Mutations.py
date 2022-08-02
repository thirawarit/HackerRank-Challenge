def mutate_string(string, position, character) :
    # You have to convert the string to a list and then change the value.
    box = list(string)
    box[position] = character
    # Then, you take the list and join it together.
    mutate_string = ''.join(box)
    return(mutate_string)

if __name__ == '__main__' :
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)