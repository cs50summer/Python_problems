#There are n stairs, a person standing at the bottom wants to 
#climb stairs to reach the nth stair. The person can climb either 1 stair or 2 stairs at a time, the task is to count the number of ways that a person can reach at the top.
# Input: n = 1
#Output: 1 There is only one way to climb 1 stair
#Input: n=2
#Output: 2 There are two ways: (1, 1) and (2)
#Input: n = 4
#Output: 5 (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

#Solution
# After interating through a few examples within 10 , following algorithm solves all cases 
# If n is 1 and not 0 then there is only 1 permutation
# if n is an even number less than 4 then 2 permutations
# If n is an odd number between 1 to 4 then number of permuations is count plus number divided by 2 plus 1
# If n is even number greater than 4 , then count is count plus teh number itself and if its an odd number greater than 4 then its count plus number -1 
# count is initialized when it is postive and greater than 1 

def climbing_stairs(n):
    if n>=1:
        count=1
    if(n%2==0):
        count=count+1
    if(n>1 and n%2!=0):
        m=int((n/2))+1
        count=count+m
    if (n > 4 and n % 2 == 0):
        # m=int((n/2))+1
        count = count + n
    #for 1 majority count
    if(n>=4):
        count=count+(n-1)

    return count



print(climbing_stairs(7))