#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.
#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4]

def plus_one(x):
    #intialize the values for computation of integer form the list
    p=len(x)
    val=1
    sum=0
    #in this loop iterating to calculate integer value
    for i in range (len(x)):
        p=len(x)-i
        val = 1
        num=x[i]
        while(p>1):
            val=val*10
            p=p-1
        final_num = num*val
        sum+=final_num
        print("sum=",sum)
    sum=sum+1
    print("sum=", sum)

    l=[]
    #init an empty list and using that to append the list values obtained from the integer value
    while (sum>0):
        n=sum%10
        print(n)
        l.append(n)
        sum=int(sum//10)
        print(sum)


    l.reverse()
    return l

print(plus_one([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]))


""""

This way is bad way , because the digit next to 9 can be either 9 or 2 ...which means , it is hard to guess
def plus_one(x):
    l=len(x)-1

    if(x[l]<9):
        x[l]+=1
    #print (x[l])
    elif(x[l]==9):
        x[l]=0
        for i in range (l):
            x[i]+=1
    print(x)

The pseudocode discussion :
Obtain numbers

1. Iterate through the array --(p=len(arr))   for i,p in range len(arr)-1: 
2. Get the individual digits   num=arr[i]
3. multiply it with the place value : To do figure out the place value (while p!=1) val=1 , val*10 ,p-- and multiply that many times with 10 -- final num 
4. add it to the sum : sum+=final_num 

Reverse the process
1. Obtain the number -- sum=sum +1
2. Count the number of digits -- / create empty list l[]
3. divide the digt by 10 and get the remainder while sum>0 num =sum%10 
4.store it in a list  l.append(num) , num=num/10
5. reverse the list l.reverse()

Step 3 --for obtain numbers 
place value
val=1
p=len(arr)  --3
while(p!=1):
  val=val*10   --100
   --p         --1

final_num =value*arr[i]


-----------------------
-----------------------
-----------------------
l[len(arr)-1] <=9
l[len(arr)-1]+=1

else:
for i in range len(arr)-2:
   l[i]+=1

l[len(arr)-1]=0




"""
#