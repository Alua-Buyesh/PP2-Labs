def spy_game(nums):
    res = 0
    for i in range(len(nums)):
        if res < 3 and nums[i] == 0:
            res += 1
        elif nums[i] == 7:
            res += 1

    if res == 3:
        print("True")
    else:
        print("False")

spy_game([0, 0, 7]) 
spy_game([0, 7, 7]) 
spy_game([0, 1, 2, 4, 0, 7, 5, 0, 0, 7])
