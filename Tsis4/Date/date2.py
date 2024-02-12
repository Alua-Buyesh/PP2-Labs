import datetime

x=datetime.datetime.now()
yesterday = x - datetime.timedelta(days=1)
today = x
tomorrow = x + datetime.timedelta(days=1)

print("Yesterday:", yesterday.strftime("%x"))
print("Today:", today.strftime("%x"))
print("Tomorrow:", tomorrow.strftime("%x"))
