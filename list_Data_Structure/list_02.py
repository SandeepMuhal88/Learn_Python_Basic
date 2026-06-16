l2=[45, 67, 89, 12, 34, 56, 78]

# count=0

# for i in range(len(l2)):
#     if i%2==0:
#         count+=1
#         print("Element at index",i,"is",l2[i])
# print("Total count of elements at even indices:", count)

# key = 34  # Example key to search for

# for i in range(len(l2)):
#     if key==l2[i]:
#         print("Element found at index", i)
#         break
# else:    print("Element not found in the list.")

# num = input("Enter size of list: ")
# my_list = []
# for i in range(int(num)):
#     element = input("Enter element: ")
#     my_list.append(element)
# print("Original list:", my_list)


# Take input only numbers

num = input("Enter size of list: ")
my_list = []
for i in range(int(num)):
    while True:
        element = input("Enter a number: ")
        if element.isdigit():  # Check if the input is a digit
            my_list.append(int(element))  # Convert to integer and append
            break
        else:
            print("Invalid input. Please enter a number.")
print("Original list:", my_list)