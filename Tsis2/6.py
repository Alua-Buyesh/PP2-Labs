i = 1
while i < 10:
    i += 1
    print(i)
else:
    print("less than 11")

names =["Jason","Odet","Clara","Nill"]
for x in names:
    print(x)

names =["Jason","Odet","Clara","Nill"]
for x in names:
    if x == "Clara":
     continue
    print(x)

for x in range(6):
   print(x)

for x in range(6):
   if x==3:
      break
   print(x)