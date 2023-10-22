import hashlib

# Define a dictionary to store user information
users = {
    "admin": {
        "password": hashlib.sha256("password123".encode()).hexdigest(),
        "email": "admin@example.com"
    },
    "user1": {
        "password": hashlib.sha256("user1pass".encode()).hexdigest(),
        "email": "user1@example.com"
    }
}


# Function to register a new user
def register_user(username, password, email):
    if username in users:
        return False  # User already exists
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = {"password": hashed_password, "email": email}
    return True


# Function to authenticate user credentials
def authenticate(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == users[username]["password"]:
            return True
    return False


# Main program
def main():
    print("User Credentials Authenticator")
    print("-----------------------------")

    while True:
        print("1. Logon")
        print("2. Sign Up")
        print("3. Leave")

        choice = input("Please select choices 1, 2, or 3 ")

        if choice == "1":  # Login
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            if authenticate(username, password):
                print("Authentication is successful! Welcome, " + username + "!")
                print("Email:", users[username]["email"])
            else:
                print("Authentication has failed. Access has been denied.")

        elif choice == "2":  # Register
            username = input("Please enter a new username: ")
            password = input("Please enter a new password: ")
            email = input("Please enter your email: ")

            if register_user(username, password, email):
                print("Registration is successful! You can now log in.")
            else:
                print("Username already exists. Please choose another username.")

        elif choice == "3":  # Exit
            break
        else:
            print("Your choice is invalid. Please select choices 1, 2, or 3.")


if __name__ == "__main__":
    main()
