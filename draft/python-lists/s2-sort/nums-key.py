def mOf2(el):
    return el % 2 == 0
nums = [7,3,5,6,1,0,0,4,9,9]
nums.sort(key=mOf2, reverse=True)
print(nums) # [9, 9, 7, 6, 5, 4, 3, 1, 0, 0]

