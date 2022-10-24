import re
def fun(s):
    # return True if s is a valid email, else return False
    '''
    for i in range(len(s)) :
        userweb_ex = s[i].split('.')
        user_web = userweb_ex[0].split('@')
        userweb_ex.insert(0,user_web)
    uwe = re.split('@|\.',s)
    print(uwe)
    user = bool(re.search('[^a-zA-Z0-9_-]',uwe[0]))
    webuser = bool(re.search('[^a-zA-Z0-9]',uwe[1]))
    exten = bool(re.search('[^a-zA-Z]',uwe[2]))
    if not (user and webuser and exten):
        return(True)
    else:
        return(False)
    '''
    return True if re.search("^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s) else False
    #return True if re.search("^[\w]+\.[\w\.]+$", s) else False
s = 'brian23@hackerrank.com'
#s = ['1.111']
x = list(filter(fun, s))
print(x)
