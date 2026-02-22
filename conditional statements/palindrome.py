word=input("Enter a line:- ")
# Logic to check whether the given string is palindrome or not
print("The given string is:- ",word)
word=word[::-1]
print("The given string is:- ",word)

if word==word[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")