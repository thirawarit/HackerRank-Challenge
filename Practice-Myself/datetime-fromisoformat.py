from datetime import datetime, timedelta
x = datetime.fromisoformat('2015-05-10 13:54:36.000-07:00')
x = datetime.strptime('May-10-2015','%b-%d-%Y')
t1 = 'Sat 02 May 2015 19:54:36 +0530'
t1 = datetime.strptime(t1, '%a %d %b %Y %X %z')
t2 = 'Fri 01 May 2015 13:54:36 -0000'
t2 = datetime.strptime(t2, '%a %d %b %Y %X %z')
print(t1, t2,abs(t1-t2).total_seconds(), sep='\n')