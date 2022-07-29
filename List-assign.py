if __name__ == '__main__':
    N = int(input())
    answer = []
    for _ in range(N) :
        a = input().split()
        if a[0] == "insert" :
            #'insert', int('i'), int('e') : Insert integer e at position i.
            answer.insert(int(a[1]),int(a[2]))
        elif a[0] == "print" :
            #'print' : Print the list.
            print(answer)
        elif a[0] == "remove" :
            #'remove', int('e') : Delete the first occurence of integer e.
            answer.remove(int(a[1]))
        elif a[0] == "append" :
            #'append', int('e') : Insert integer e at the end of the list.
            answer.append(int(a[1]))
        elif a[0] == "sort" :
            #'sort' : sort the list.
            answer.sort()
        elif a[0] == "pop" :
            #'pop' : Pop the last element from the list.
            answer.pop()
        else :
            #'reverse' : Reverse the list.
            answer.reverse()