def f(tup):
    return all(tup)

tup = (True, True, False, True)
t=(True,True)
s=(False,  False, False)

print("All elements are true:", f(tup))
print("All elements are true:", f(t))
print("All elements are true:", f(s))
