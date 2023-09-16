# Kadane's Algorithm - GeeksForGeeks problem

# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# Brute force approach : using nested loops... but time limit will exceed
def maximumsum(arr):
    sum = 0
    answer = arr[0]
    for i in range(len(arr)):
        sum = 0
        for j in range(i+1, len(arr)):
            sum += arr[j]
            answer = max(answer,sum)
    return answer


# Kadane's Algorithm

def kadane(arr,size):
    max_so_far = -1
    max_ending_here = 0
    for i in range(0,size):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

arr = [1,2,3,-2,5]
print(kadane(arr,len(arr)))
arr= [-1,-2,-6,-4,-5]
print(kadane(arr,len(arr)))
arr = [-2, 1 ,-3 ,4 ,-1 ,2, 1 ,-5 ,4]
print(kadane(arr,len(arr)))
# print(maximumsum(arr))
