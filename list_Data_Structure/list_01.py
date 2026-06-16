# l1=[23,14,12,57,89,53,90]

# print(l1)

# print(l1[-4])

# print(l1[2:5])
# # [12, 57, 89]



dataset = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png"]

# Extracting mini-batches (Slicing)
batch_1 = dataset[0:2]    # ['img1.png', 'img2.png']

# Reversing a list via striding
reversed_data = dataset[::-1] 

# Slicing for in-place modification
dataset[1:3] = ["augmented_2.png", "augmented_3.png"]

