x="gfrtsfsgxbvcnds"
print(len(x))

x=90854326789
print(len(str(x)))

y="ujgfmfvnbb"
print(y[0])

for x in "kuhnia":
  print(x)

txt = "have a nice day"
print("day" in txt)
print("night" in txt)

txt = "do you have candy"
if "candy" in txt:
  print("Yes, 'candy' in txt")

txt = "i havent money"
print("money" not in txt)

txt = "i earn bitcone"
if "...." not in txt:
  print("No, '....' is NOT present.")

b = "Hilode KBTU"
print(b[2:5])

b = "Daycare"
print(b[:5])

b = "douremember?"
print(b[2:])

b = "abcdersdt"
print(b[-5:-2])

a = "myname"
print(a.upper())

a = "YURDOG"
print(a.lower())

a = "      Bye        "
print(a.strip())

a="good night"
print(a.replace('g','n'))

a="daaaaay, was, amazing"
print(a.split(','))

a="have"
b="flower"
print(a+" "+b)

pen = 108
txt = "i have {} pen"
print(txt.format(pen))

a="ghj"
b="khjh"
c="hvh"
rer=".... {} <<<<< {} PPPPPPP {}"
print(rer.format(a,b,c))

h = 3
q = 567
w = 49.95
i = ".....{2}.....{0}.....{1}"
print(i.format(h, q, w))

txt = "i have \"good\" friend"
print(txt)
