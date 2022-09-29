import time
from datetime import date
def birthday_count(year : int = ...,month : int = ...,day : int = ...):
    today = date.today()
    my_bday = date(
        year=year, 
        month=month, 
        day=day
    )
    if my_bday < today:
        my_bday = my_bday.replace(year=today.year + 1)
    return(abs(my_bday - today).days)
if '__main__' == __name__:
    
    today = date.today()
    #print(today)   #yyyy-mm-dd
    check_equiv = (today == date.fromtimestamp(time.time()))
    print(check_equiv)  #date.today() that is equivalent to date.fromtimestamp(time.time()).
    my_bday = date(
        year=int(input('Year : ')), 
        month=int(input('Month : ')), 
        day=int(input('Day : '))
    )
    if my_bday < today:
        #return a new date with the 'attri.' of classname(today) + 1
        my_bday = my_bday.replace(year=today.year + 1)
    #print(my_bday) #yyyy-mm-dd
    time_to_bday = abs(my_bday - today)
    print(time_to_bday.days,'days')
    
    '''
    print(birthday_count(
            year=int(input('Year : ')), 
            month=int(input('Month : ')), 
            day=int(input('Day : '))
        )
    )
    '''
    