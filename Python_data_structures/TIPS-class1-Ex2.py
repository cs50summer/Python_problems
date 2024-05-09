#Given an array of unsorted integers and a number k. Check if there is a pair of integers in the array that sums to K.
#Write an optimized and brute force solution both. Provide the Time and Space complexity of each

def unsortedsum(nums,k):
    #find the length of the list / array
    l=len(nums)
    #Assign the indices as first and second from the list
    i=0
    j=i+1


    #Traverse through the list to find out which combination returns the sum
    #There is a double iteration to make sure every combination is tried iteratively through the list
    for _ in  range (l-i):
        for _ in range (l-i-1):
            sum=nums[i]+nums[j]
            if(sum==k):
                return (True,i,j)
            elif(sum!=k):
               j=j+1
        #The keeping first index constant , iterate through every other index ,then increase starting index to achieve next iteration
        i=i+1
        j=i+1


    #If there is no sum present , then return False
    return False


#Call the function and Print the result
print(unsortedsum([3,0,4,1,6,2],5))

# The Time Complexity is T= O(n^2/2)=O(n^2)
# The Space complexity is S= O(n^2) ( Same as time , since it would fill up half the array ...if array size is 7
# the iteration j index takes sum 5 spaces , j index iteration 2 takes 4 spaces , j index Iteration 3 takes 3 spaces....
# The iteration i index takes (5,4,3,2,1) i index iteration 2 takes (4,3,2,1)