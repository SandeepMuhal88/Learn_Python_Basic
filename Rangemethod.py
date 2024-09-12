# x=range(5)
# print(x)
# for e in range(1,50,2): # (start,stop,step)
#     print(e)

# for el  in range(101,1,-1):
#     print(el)

#  Table printing

# n=int(input("Enter a number:- "))
# for el in range(n,n*11,n):
#     print(el)

# n=int(input("Enter a number:- "))
# sum=0
# # for el in range(1,n+1):
# #     sum+=el
# #     print(el)
# # print("Total sum :-",sum)
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

#  Print factorial number:- usind rang method 
n=int(input("Enter a number to print factorial value:- "))
fact=1
# for el in range(1,n+1,1):
#     fact*=el
# print(fact)
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)
