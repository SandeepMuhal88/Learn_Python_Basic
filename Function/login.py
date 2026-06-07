# def login(username, password):
#     # This is a placeholder function for user login
#     # In a real application, you would check the username and password against a database
#     if username == "admin" and password == "password":
#         return "Login successful!"
#     else:
#         return "Invalid username or password."
# # Example usage
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# result = login(username, password)
# print(result)


# Upgrade  the login function to include a simple user authentication system with a predefined list of users and passwords.
list_of_users = {
    "admin": "password",
    "user1": "pass123",
    "user2": "mypassword"
}



def login(username, password):
    if username in list_of_users:
        if list_of_users[username] == password:
            return "Login successful!"
    return "Invalid username or password."  