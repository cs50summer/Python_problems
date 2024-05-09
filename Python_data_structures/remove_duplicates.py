# what is challenging
# integer array - what is integer array - dont know how to handle integer array -- is it the same as List , how is teh handling different here
# two arrays - int] nums and int[] expectednums
# lets do the comparison of list vs array in python
# then do the problem

import array

def remove_duplicates():
    nums=[1,2,3,4,6,6,6,6,6]
    new_nums=list(range(len(nums)))

    if len(nums) == 0 or len(nums) == 1:
        return

    j=0


    for i in range (0,len(nums)-1):
        if nums[i]!=nums[i+1]:
            new_nums[j]=nums[i]
            j+=1

    new_nums[j]=nums[len(nums)-1]
    j=j+1

    return new_nums



    #for i in new_nums:
        #print(i)


print(remove_duplicates())