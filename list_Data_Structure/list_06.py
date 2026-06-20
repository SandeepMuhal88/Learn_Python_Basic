# Q13. Maximum Subarray Sum

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum
# Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = max_subarray_sum(arr)
print("Maximum subarray sum is:", result)
