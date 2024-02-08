def f(nums):
    unq=[]
    for i in nums:
        if i not in unq:
            unq.append(i)
    return unq

unq=f([1,2, 2, 3,4,4,4,4,5])
print(unq)