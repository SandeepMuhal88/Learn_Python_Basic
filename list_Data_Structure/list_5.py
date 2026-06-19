# Rotate List Right by K
arr = [1,2,3,4,5]
k = 2

# Rotate the list to the right by k positions
k = k % len(arr)  # Handle cases where k is greater than the length of the list
rotated_arr = arr[-k:] + arr[:-k]
print("The rotated list is: ", rotated_arr)
