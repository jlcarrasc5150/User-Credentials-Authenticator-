# Import the hashlib module for password hashing

# Create a dictionary to hold user information
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
    # Check if the username already exists in the dictionary
    if username in users:
        return False  # User already exists
    # Hash the provided password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Store the user's information in the dictionary
    users[username] = {"password": hashed_password, "email": email}
    return True

# Function to authenticate user credentials
def authenticate(username, password):
    # Check if the username exists in the dictionary
    if username in users:
        # Hash the provided password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Compare the hashed password with the stored password
        if hashed_password == users[username]["password"]:
            return True  # Authentication successful
    return False  # Authentication failed

# Main program
def main():
    print("User Credentials Authenticator")
    print("-----------------------------")

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":  # Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if authenticate(username, password):
                print("Authentication successful! Welcome, " + username + "!")
                print("Email:", users[username]["email"])
            else:
                print("Authentication failed. Access denied.")

        elif choice == "2":  # Register
            username = input("Enter a new username: ")
            password = input("Enter a password: ")
            email = input("Enter your email: ")

            if register_user(username, password, email):
                print("Registration successful! You can now log in.")
            else:
                print("Username already exists. Please choose another username.")

        elif choice == "3":  # Exit
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
