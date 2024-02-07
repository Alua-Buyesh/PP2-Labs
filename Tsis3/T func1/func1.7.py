def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            print("True")
            return 0
    print("False")
    return 0


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])