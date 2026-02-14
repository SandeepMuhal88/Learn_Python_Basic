#swap number without using third variable
a=int(input("Enter first number:- "))
b=int(input("Second number:- "))
print("Before swap a=",a,"b=",b)
a,b=b,a
print("After swap a=",a,"b=",b)