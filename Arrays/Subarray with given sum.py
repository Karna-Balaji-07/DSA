# Subarray with given sum { GeeksForGeeks }
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements from 2nd position to 4th position is 12.
#
# Input:
# N = 10, S = 15
# A[] = {1,2,3,4,5,6,7,8,9,10}
# Output: 1 5
# Explanation: The sum of elements from 1st position to 5th position is 15.


# Approach 1
def Subarray(arr,n,x):
    # arr = array
    # n = size of array
    # x = sum
    for i in range(0,len(arr)-1):
        sum = 0
        sum += arr[i]
        for j in range(i+1,len(arr)):
            sum += arr[j]
            if sum == x:
                return [i+1,j+1]
# Time complexity is O(n^2)......too much large input is impossible in this case

#Approach 2
def sub(arr,x,n):
    i = 0
    j = 0
    sum = 0
    if x == 0:
        return -1
    while j < n:
        sum += arr[j]
        while sum > x:
            sum -= arr[i]
            i+=1
        if sum == x:
            return i+1,j+1
        j+=1
    return -1

# arr = [1,2,3,7,5]
# x = 12
arr = [142 ,112 ,54 ,69 ,148 ,45 ,63 ,158 ,38 ,60 ,124 ,142 ,130 ,179 ,117 ,36 ,191 ,43 ,89 ,107 ,41 ,143 ,65 ,49 ,47 ,6 ,91 ,130 ,171 ,151 ,7 ,102 ,194 ,149 ,30 ,24 ,85 ,155 ,157 ,41 ,167 ,177 ,13 ,109 ,145 ,40 ,27 ,124 ,138 ,139 ,119 ,83 ,130 ,142 ,34 ,116 ,40 ,59 ,105 ,131 ,178 ,107 ,74 ,187 ,22 ,146 ,125 ,73 ,71 ,30 ,178 ,174, 98 ,113]
x = 665
n =len(arr)
#res = Subarray(arr,n,x)
#print(res)
res = sub(arr,x,n)
print(res)


# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, sum_):
        # Initialize curr_sum as
        # value of first element
        # and starting point as 0
        A = []
        curr_sum = arr[0]
        start = 0

        # Add elements one by
        # one to curr_sum and
        # if the curr_sum exceeds
        # the sum, then remove
        # starting element
        i = 1
        while i <= n:

            # If curr_sum exceeds
            # the sum, then remove
            # the starting elements
            while curr_sum > sum_ and start < i - 1:
                curr_sum = curr_sum - arr[start]
                start += 1

            # If curr_sum becomes
            # equal to sum, then
            # return true
            if curr_sum == sum_:
                A.append(start + 1)
                A.append(i)
                return A

            # Add this element
            # to curr_sum
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1

        # If we reach here,
        # then no subarray
        A.append(-1)
        return A