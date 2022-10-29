import re
def rep(s: str) -> str:
    '''
    Print the first occurrence of the repeating character. \n
    If there are no repeating characters, print "don't have pattern in any characters"
    '''
    # (...)\number{}
    # \number being a number of group. Groups are numbered starting from 1.
    
    # group(0):22ccc333 | group(1):2 | group(2):c | group(3):3
    pattern = r'([A-Za-z0-9])\1([\w])\2{2}([\w])\3{2}'
    #return -> 22ccc333
    # group(0):dddd | group(1):d
    pattern = r'([A-Za-z0-9])\1+'
    #return -> dddd
    
    x = re.search(pattern, s)
    return x.group(0)

def plookba(s: str) -> str:
    '''
    The positive lookbehind assertion    \n
    (?<=...) Lookbehind    \n
    
    (?=...)  Lookahead    \n
    '''
    pattern = r'(?<=[a-zA-Z]{3})\w(?=[a-zA-Z]{3})'
    #return -> dddd
    
    x = re.findall(pattern, s)
    return x

s = "1dddd22ccc333bb4444a"
s2 =  "aaa1bbb2ccc"
print(rep(s), plookba(s2))