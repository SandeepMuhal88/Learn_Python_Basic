def login(username, password):
    # This is a placeholder function for user login
    # In a real application, you would check the username and password against a database
    if username == "admin" and password == "password":
        return "Login successful!"
    else:
        return "Invalid username or password."
# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")
result = login(username, password)
print(result)
