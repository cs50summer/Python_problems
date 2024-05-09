import array

def remove_duplicates():
    nums=[1,1,2,2,3,4,4,5,6,6,6,6,6,7,7,7,7,7,7,8,8,9,]

    if len(nums) == 0 or len(nums)==1:
        return 0

    #nums[:] = [nums[0]]+[nums[i] for i in range(1,len(nums)) if nums[i] != nums[i-1]]
    return len(list(set(nums)))
    #return nums

print(remove_duplicates())