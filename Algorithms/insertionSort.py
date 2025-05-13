#Take the first value from the unsorted part of the array.
#Move the value into the correct place in the sorted part of the array.
#Go through the unsorted part of the array again as many times as there are values.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array)

#time complexity  O(n/2*n)=O(n square)
