# Remove duplicates from sorted array

def remove(arr):
    j = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j += 1

    return j


arr = [1,1,1,2,3,4,5,6]
print(remove(arr))

