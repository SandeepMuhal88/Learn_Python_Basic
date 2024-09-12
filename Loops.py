# 1 to 100 print usig whle loop
# i=1
# while i<=100:
#     print(i)
#     i+=1
# Reverse order
# k=100
# while k>=1:
#     print(k)
    # k-=1
# Table printing user input
# x=int(input("Enter a numer:-"))
# # n=int(input("Enter a number:-"))
# print("Print the table")
# i=1
# while i<=10:
#     k=x*i
#     print(k)
#     # print(x*i)
#     # print(n*i)
#     i+=1

# Print the list using while loops
# List=[12,5,2,36,52,78,96,5,36,100,5,35,39,10]
# i=0
# while i<=len(List)-1:
#     print(List[i])
#     i+=1
# Find number 
n=int(input("Enter number you want to search:- "))
num=[12,5,2,36,52,78,96,5,36,100,5,35,39,10]
i=0
while i<=len(num):
    if num[i]==n:
        print("found number:-",num[i])
        break
    else:
        print("This number is not present in list:- ",n)
        break
i+=1