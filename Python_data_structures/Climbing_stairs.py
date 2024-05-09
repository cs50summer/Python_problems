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