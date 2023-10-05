# Remove element

def remove(arr,key):
    index = 0
    for i in range(1,len(arr)):
        if arr[i] != key:
            arr[index] = arr[i]
            index += 1
    return index

arr = [1,2,2,2,3,4,5,4,5,6,6,6,7]
key = 2
print(remove(arr,key))
