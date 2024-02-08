def z(nums):
    for i in range(len(nums)):
        t=""
        for j in range(nums[i]):
            t+="*"
        print(t)

nums=[3, 8, 5]
z(nums)