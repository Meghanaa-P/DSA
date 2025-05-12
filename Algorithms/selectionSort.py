#Go through the array to find the lowest value.
#Move the lowest value to the front of the unsorted part of the array.
#Go through the array again as many times as there are values in the array.

arr=[8,3,7,2,9,1,5,0]
n=len(arr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"Sorted array: {arr}")
