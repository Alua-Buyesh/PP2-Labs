import datetime

x=datetime.datetime.now()
y=int(x.strftime("%d"))-5
print(y)