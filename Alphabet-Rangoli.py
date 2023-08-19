def print_rangoli(size):
    # your code goes here
    
    """
    ord() >> converts an integer representing the specified Unicode character.
    'a' was converted an integer is >> 97
    {'b', 'c', 'd', ... >>>> 98, 99, 100, ...}
    chr() >> Returns a character from the specified Unicode code.

    -----------------------------------------------------------------------------
    สำหรับ list การเขียน[:num] นั่นหมายถึง การเรียกใช้ข้อมูล โดยเริ่มจากตำแหน่ง 0 จนไปถึง num-1
    """
    
    if size == 1 :
        print("a")
        return()

    #TOP
    for i in range(size):       #Size : 5 >> [0,1,2,3,4] 5 values
        #Left-Center-Right

        print('-'.join(map(chr,range(97-1+size,97,-1)[:i])).rjust((size)*2-3,'-')
              + chr(range(97-1+size,97-1,-1)[i]).center(3,'-')
              + '-'.join(map(chr,range(97,97+size)[size-i:])).ljust((size)*2-3,'-')
              )
        #range >> [e,d,c,b] get position[0:0+]      >> []   >> [e]  >> [e,d]  >> [e,d,c]    >> [e,d,c,b]
        #range >> [e,d,c,b,a] get position[0 to 4]  >> [e]  >> [d]  >> [c]    >> [b]        >> [a]
        #range >> [b,c,d,e] get position[5--:4]     >> []   >> [e]  >> [d,e]  >> [c,d,e]    >> [b,c,d,e]
    
    #BUTTOM
    for j in range(size,1,-1):  #Size : 5 >> [5,4,3,2] 4 values
        #Left-Center-Right

        #[e,d,c,b]    [e,d,c,b]     [b,c,d,e]
        print('-'.join(map(chr,range(97-1+size,97+1,-1)[:j-2])).rjust((size)*2-3,'-')+chr(range(97+1,97+size)[size-j]).center(3,'-')+'-'.join(map(chr,range(97+2,97+size)[size-j:])).ljust((size)*2-3,'-'))
        #range >> [e,d,c] get position[0:3--]       >> [e,d,c] >> [e,d]  >> [e]  >> []
        #range >> [b,c,d,e] get position[0 to 3]   >> [b]     >> [c]    >> [d]  >> [e]
        #range >> [c,d,e] get position[0+:3]       >> [c,d,e] >> [d,e]  >> [e]  >> []

    #print('-'.join(map(chr,range(97-1+size,97-1,-1)[:5])).rjust((size)*2-3,'-'))
    
       
'''
    #from discussions good idea!!
    
    import string
    alpha =list(string.ascii_lowercase)
    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        print(s)
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        print(L)
    print('\n'.join(L[:0:-1]+['*']+L))
'''    


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


"""
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""