
#Go through the array, one value at a time.
#For each value, compare the value with the next value.
#If the value is higher than the next one, swap the values so that the highest value comes last.
#Go through the array as many times as there are values in the array.

array=[8,5,2,7,9,3,4,1,0]
n=len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j+1],array[j]=array[j],array[j+1]
print(f"Sorted Array = {array} ")


#The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it.
# So for an array of n values, there must be n such comparisons in one loop.  
#This means there are n⋅n comparisons done in total, so the time complexity for Bubble Sort is: O(n square)