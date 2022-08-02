def count_substring(string, sub_string) :
    count_str = 0
    for i in range(len(string)) :
        # String[i:] start i to end(-1) ex. 'abcde'
        # string[1:] >> 'bcde'
        # startwith(prefix, start = 1, end = 0)
        if string[i:].startswith(sub_string) :
            count_str += 1
    return(count_str)
if __name__ == '__main__' :
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)