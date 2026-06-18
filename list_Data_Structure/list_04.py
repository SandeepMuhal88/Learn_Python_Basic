# num = int(input("Enter size of the list: "))

# my_list = []

# for i in range(num):
#     element = input("Enter element: ")
#     my_list.append(element)
# print("The list is: ", my_list)

# # output:

# reverse without using reverse function

arr = [10, 20, 30, 40, 50]

# print(arr[::-1])  # Output: [50, 40, 30, 20, 10]

# reversed_arr = []
# for i in range(len(arr)):
#     reversed_arr.append(arr[len(arr) - 1 - i])
# print("The reversed list is: ", reversed_arr)


arr = [12, 45, 2, 41, 31, 10]
# sorted_arr = sorted(arr)
# print("The sorted list is: ", sorted_arr) 

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("The sorted list is: ", arr)

# find second largest element in the list

second_largest = arr[-2]
print("The second largest element is: ", second_largest)

#remove duplicates from the list
arr = [1,2,2,3,4,4,5,5,5]

unique_arr = []
for element in arr:
    if element not in unique_arr:
        unique_arr.append(element)
print("The list with duplicates removed is: ", unique_arr)