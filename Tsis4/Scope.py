#Examples
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

def myfunc():
  global x
  x = 100

myfunc()

print(x)