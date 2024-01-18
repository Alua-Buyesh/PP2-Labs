x='Me'
def ad():
    print("You "+x)

ad()

y = "awesome"

def myfunc():
  y = "witch"
  print("Me is " + y)

myfunc()
print("Me is " + y)

x = "awesome"

def huy():
  global x
  x = "ploho"

myfunc()

print("Delo idet " + x)