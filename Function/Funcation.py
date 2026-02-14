# def sum(a,b):
#     s=a+b
#     return s

# a=int(input("Enter first number:- "))
# b=int(input("Enter Second number:- "))
# print("Sum of two number:-",sum(a,b))

# Table printin function
def table(n):
    sum=0
    for el in range(1,11):
     sum=n*el
     print(sum)
        # sum*=el
        # print(sum)
         
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

def demo(n):
   if(n==0):
      return
   print(n)
   demo(n-1)

#    Print factorial number:- using recursion
def Factorial(n):
   if(n==0 and n==1):
      return 1
   else:
      return factorial(n-1)*n
   
# Recursion in function
intput_user=int(input("Enter first number:- "))
# table(intput_user)
# print(factorial(intput_user))
# print(demo(intput_user))
# demo(intput_user)
print(Factorial(intput_user))
