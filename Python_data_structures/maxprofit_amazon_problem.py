#finding the max sum profit wrt to how many values are to be removed, k.
#the values are to be removed are actually opposites in a pie contiguous chart
#the numbers given in the profit array are inserted counter clockwise, starting from the 9:00 position, within the contiguous pie chart
#let's assume that the pie chart will be always divided into 6 pieces....

k = 2
profit = [1,5,1,3,7,-3]

def maxProft(k, profit):
    n = len(profit)
    #print(n) = 6
    start, end = 0, n-3
    temp = []
    while end < len(profit):

        leftover_sum= sum(profit) - (profit[start] + profit[end])


        temp.append(leftover_sum)
        #print(leftover_sum)
        start +=1
        end +=1

    return max(temp)

result = maxProft(k,profit)
print(result)