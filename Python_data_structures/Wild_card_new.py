import string



nums = str(input("What number? (in 0s and 1s with missing digits, ex: 100?1, 1?1 "))

def Wildcard(nums):

    # initializing the variables as start index , end index and index of the wildcard
    startIndx=0
    endIndx=len(nums)
    #indx=-1

    try:
        indx=nums.index("?")
    except:
        return nums
    # In python , trying to find index of '?' . Using the nums.index('?') gives error and exception when no wildcard found . We will need this wildcard check everytime in the recursive call
    #for char in nums:
    #   if char=='?':
    #        indx=nums.index("?")
            #print(indx)

   # After we find the index of question mark , it is about replacing the question mark in that index
   # If the input has no '?' then return it back
   # if(indx==-1):
    #    return nums
    #If the string has '?' in the end of the string , then simply replace that one instance and return the program
    if(indx==endIndx-1):
        nums1=nums.replace('?','0')
        nums2 = nums.replace('?', '1')
        return nums1 +","+nums2
    #If the string has '?' in first character , replace that with 1, 0 and place recursive call for each occurence of '?'

    if(indx==0):
        nums1="1"+nums[indx+1:endIndx]
        nums2="0"+nums[indx+1:endIndx]
        return Wildcard(nums1)+","+Wildcard(nums2)
    # If the string has '?' in any index in between , replace that with 1, 0 and place recursive call for each occurence of '?'
    elif(indx<endIndx-1):
        nums1=nums[startIndx:indx]+"1"+nums[indx+1:endIndx]
        nums2=nums[startIndx:indx]+"0"+nums[indx+1:endIndx]
        return Wildcard(nums1)+","+Wildcard(nums2)

    return nums



result = Wildcard(nums)
print(result)

