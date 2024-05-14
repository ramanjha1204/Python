# Bank Application
users = {}


def signup():
    print("===== Sign Up =====")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Add user to the dictionary
    users[email] = {"name": name, "password": password, "balance": 0}

    print("Sign up successful!")


def login():
    print("===== Login =====")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if user exists and password is correct
    if email in users and users[email]["password"] == password:
        print("Login successful!")
        return email
    else:
        print("Invalid email or password.")
        return None


def deposit(email):
    print("===== Deposit =====")
    amount = float(input("Enter the amount to deposit: "))

    # Update user's balance
    users[email]["balance"] += amount
    print(f"Deposit of {amount} successful!")


def withdrawal(email):
    print("===== Withdrawal =====")
    amount = float(input("Enter the amount to withdraw: "))

    # Check if user has sufficient balance
    if amount <= users[email]["balance"]:
        # Update user's balance
        users[email]["balance"] -= amount
        print(f"Withdrawal of {amount} successful!")
    else:
        print("Insufficient balance.")


def forgot_password():
    print("===== Forgot Password =====")
    email = input("Enter your email: ")

    # Check if user exists
    if email in users:
        new_password = input("Enter a new password: ")

        # Update user's password
        users[email]["password"] = new_password
        print("Password reset successful!")
    else:
        print("User does not exist.")


# Bank Application
def main():
    while True:
        print("\n===== Welcome to The Bank of Jaipur =====")
        print("1. Sign Up")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Forgot Password")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            signup()
        elif choice == "2":
            email = login()
            if email:
                # User logged in successfully
                while True:
                    print("\n===== Welcome to Bank =====")
                    print("1. Deposit")
                    print("2. Withdrawal")
                    print("3. Logout")

                    user_choice = input("Enter your choice (1-3): ")

                    if user_choice == "1":
                        deposit(email)
                    elif user_choice == "2":
                        withdrawal(email)
                    elif user_choice == "3":
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Please login to continue.")
        elif choice == "3":
            print("Please login to continue.")
        elif choice == "4":
            print("Please login to continue.")
        elif choice == "5":
            forgot_password()
        elif choice == "6":
            print("Thank you for using the Bank Application. Goodbye!")
            break
        else:
            print("Invalid choice.")


# Run the main function
main()