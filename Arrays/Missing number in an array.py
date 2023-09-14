# Missing number in an array

def missingNumber(array, n):
    # code here
    sum = 0
    sums = 0
    # for i in range(1, n + 1):
    #     sum += i
    for i in range(0, len(array)):
        sums += array[i]

    sum = (n*(n+1)) // 2
    
    if sum != sums:
        return sum - sums

n = 5
array = [1,2,3,5]

result = missingNumber(array,n)
print(result)