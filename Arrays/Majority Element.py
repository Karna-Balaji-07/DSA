# Majority element in an array


#Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.

def Majority(arr,n):
    half = n // 2
    count = 0
    element = -1
    if n == 1:
        return arr[0]

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                element = arr[i]
                print("Count : ",count)

        if count > half:
            return element
    return -1


def majority2(arr,n):
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i] = 1

    for i,count in dict1.items():
        if count > n//2:
            return i
    return -1

arr = [3,1,3,3,2]
# arr = [1,2,3]
# arr = [15]
# arr = [9 ,14 ,10 ,10, 1, 2, 1, 7, 10, 10, 14 ,19 ,9]
n = len(arr)
till = majority2(arr,n)
print(till)
res = Majority(arr,n)
print(res)