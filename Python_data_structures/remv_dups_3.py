import array

def removeDuplicates( nums):
    # Length of the update array
    count = 0
    # Loop for all the elements in the array
    for i in range(len(nums)):
        # If the current element is equal to the next element, we skip
        if i < len(nums) - 2 and nums[i] == nums[i + 1]:
            continue
        # We will update the array in place
        nums[count] = nums[i]
        count += 1
    return nums

print(removeDuplicates([1,1,2,2,2,2,4]))