def twosum(arr,target):

    for i in arr:
        for j in arr:
            print("i is :",i,"j is :",j)
            if i+j==target:
                return i,j;


def twosumv2(arr,target):

    for i in range(len(arr)):
        for j in range(len(arr)):
            print("i is :",i,"j is :",j)
            if arr[i]+arr[j]==target:
                return i,j;





print(twosum([1,7,8,5],13))
print(twosumv2([1,7,8,5],13))
