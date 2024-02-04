def solve(numheads, numlegs):
    for i in range(1,numheads):
        if i*4+(numheads-i)*2==numlegs:
            return i
        
heads,legs=35, 94
rab=int(solve(heads,legs))
chik=heads-rab
print("rabits:",rab,"chickens", chik)
