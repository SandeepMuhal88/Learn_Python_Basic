# l1=[1, 2, 3, 4, 5, 6, 7, 8, 9]

# if 2 in l1:
#     print("Element found in the list.")
# else:
#     print("Element not found in the list.")


# l2=[45, 67, 89, 12, 34, 56, 78]

# key = 34  # Example key to search for

# for i in range(len(l2)):
#     if key==l2[i]:
#         print("Element found at index", i)
#         print("Element found in the list:", l2[i])
#         break
# else:
#     print("Element not found in the list.")

# Binary Search

# arr=[21,47,12,56,34,89,45]
# take array input from user and sort it

num = input("Enter size of list: ")
arr = []
for i in range(int(num)):
    element = input("Enter a number: ")
    arr.append(int(element))  # Convert to integer and append
arr.sort()  # Sort the array
print("Sorted array:", arr)

key = int(input("Enter the number to search for: "))

low=0
high=len(arr)-1

while low<=high:
    mid=(low+high)//2
    if key==arr[mid]:
        print("Element found at index", mid)
        print("Element found in the list:", arr[mid])
        break
    elif key>arr[mid]:
        low=mid+1
    else:
        high=mid-1
    