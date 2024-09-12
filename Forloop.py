# Use in List
# Listn=[12,5,6,3,200,46,36,78]
# for val in Listn:
#     print(val)
# Namelist=["Sandeep","Suresh","Nathu","Ramesh"]
# for i in Namelist:
#     print(i)

# # Use in tuples 
# tup=("Sandeep","Ramesh","XYz","lfufu")
# for k in tup:
#     print(k)

#     # Use in String 
# str="Sandeep"
# for c in str:
#     if(c=='d'):
#         print("d found")
#         break
#     print(c)
# else:
#     print("Not found")

# Question
List=[12,86,15,663,15,2,6,4,3,8,63,7]
n=int(input("Enter a number:- "))
for el in List:
    if(el==n):
        print("Number is found:)))",n)
        break
else:
    print("Number is not found")