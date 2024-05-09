#Given an array of sorted integers and a number k. Check if there is a pair of integers in the array that sums to K.
#Return true or False. Also mention the Time and Space complexity of your problem
#Interview time: 10-15mins
#Follow up: Return a pair of the indices instead of just existence

def sumit(nums,k):
    #find the length of the list / array
    l=len(nums)
    #Assign the indices as first and last of the list
    i=0
    j=l-1


    #Traverse through the list to find out which combination returns the sum
    for _ in range (l-1):
        sum=nums[i]+nums[j]
        if(sum==k):
            return (True,i,j)
        elif(sum>k):
            j=j-1
        else:
            i=i+1

    #If there is no sum present , then return False
    return False


#Call the function and Print the result
print(sumit([1,2,3],6))


#The Time complexity is T=O(n)
#The Space complexity is S=O(n)