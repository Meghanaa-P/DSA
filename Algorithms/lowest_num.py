array_num=[7,9,1,3,5,6]
minVal=array_num[0]
for i in array_num:
    if i<minVal:
        minVal=i
print(f"The lowest number is = {minVal}")

# time complexity is O(n)
# because if it is 50 elements in the array then the loop need to run 50 times
