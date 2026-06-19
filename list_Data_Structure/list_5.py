# Rotate List Right by K
arr = [1,2,3,4,5]
k = 2

# Rotate the list to the right by k positions
k = k % len(arr)  # Handle cases where k is greater than the length of the list
rotated_arr = arr[-k:] + arr[:-k]
print("The rotated list is: ", rotated_arr)

# Find Missing Number

arr = [1,2,4,5]

all_numbers_sum = sum(range(1, len(arr) + 2))  # Sum of first n natural numbers
arr_sum = sum(arr)
missing_number = all_numbers_sum - arr_sum
print("The missing number is: ", missing_number)
