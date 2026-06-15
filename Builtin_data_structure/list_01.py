# my_list = [1, 2, 3, 4, 5]
# print("Original list:", my_list)

# print("Every second element:", my_list[::2])


my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

for i in range(len(my_list)):
    if i % 2 == 0:
        print("Element at index", i, "is", my_list[i])
    

