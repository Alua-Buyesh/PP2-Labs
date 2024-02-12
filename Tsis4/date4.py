import datetime

def d(date1, date2):
    timedelta = date2 - date1
    return timedelta.total_seconds()

date_format = "%y-%m-%d %H:%M:%S"


x = input("Input1: ")
y = input("Input2: ")

date1 = datetime.datetime.strptime(x, date_format)
date2 = datetime.datetime.strptime(y, date_format)

dif =int(d(date1, date2)) 
if dif<0:
    dif=-dif
print("Difference in seconds:", dif)
