import re
from types import NoneType
def fun(s):
    # return True if s is a valid email, else return False
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
    
s = 'brian23@hackerrank.com'
fun(s)
