#Exersize 1-6
def function():
    i=1
    print(i)

function()

def color(red,blue,green):
    print(red)

color(777, 9 , 3)

def a(x):
    return x+7

x=3
y=a(x)
print(y)

names =["Almas","Alua","Dariga"]

def f(*name):
    print("Hello " + name[1])

f(*names)

#Examples
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))