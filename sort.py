def sortNums(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return ([1] * counts[1] + [2]* counts[2] + [3]*counts[3])

def inplace_Algo(nums):
    one_index = 0 
    index = 0
    three_index = len(nums) -1 

    while index <= three_index:
        if nums[index] == 1:
            nums[index], nums[one_index] = nums[one_index], nums[index]
            index += 1
            one_index += 1
        elif nums[index] == 2:
            index += 1 
        elif nums[index] == 3:
            nums[index], nums[three_index] = nums[three_index], nums[index]
            three_index -=1 

    return nums

lst = [3,2,1,2,3,2,1,2,3,2,3,2,3,1]
print(sortNums(lst))
print(inplace_Algo(lst))