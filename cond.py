import os

DATA_FILE = 'accounts.txt'
def load_accounts():
    accounts = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    username, password, balance = parts
                    accounts[username] = {'password': password, 'balance': float(balance)}
    return accounts

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        for username, info in accounts.items():
            file.write(f"{username},{info['password']},{info['balance']}\n")

def create_account(accounts):
    username = input("Enter new username: ")
    if username in accounts:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance. Account not created.")
        return
    accounts[username] = {'password': password, 'balance': balance}
    print("Account created successfully.")

def user_login(accounts):
    username = input("Username: ")
    password = input("Password: ")
    user = accounts.get(username)
    if user and user['password'] == password:
        print(f"Welcome {username}!")
        user_menu(accounts, username)
    else:
        print("Invalid username or password.")

def user_menu(accounts, username):
    while True:
        print(f"\n--- {username.upper()}'s ACCOUNT ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance(accounts, username)
        elif choice == '2':
            deposit(accounts, username)
        elif choice == '3':
            withdraw(accounts, username)
        elif choice == '4':
            save_accounts(accounts)
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def check_balance(accounts, username):
    balance = accounts[username]['balance']
    print(f"Your current balance is: ${balance:.2f}")

def deposit(accounts, username):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            accounts[username]['balance'] += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Invalid input.")

def withdraw(accounts, username):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > accounts[username]['balance']:
            print("Insufficient balance.")
        else:
            accounts[username]['balance'] -= amount
            print(f"${amount:.2f} withdrawn successfully.")
    except ValueError:
        print("Invalid input.")

def main():
    accounts = load_accounts()

    while True:
        print("\n=== BANK SYSTEM ===")
        print("1. Admin - Create Account")
        print("2. User - Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account(accounts)
            save_accounts(accounts)
        elif choice == '2':
            user_login(accounts)
        elif choice == '3':
            save_accounts(accounts)
            print("Thank you for using the banking app!")
            break
        else:
            print("Invalid option. Please choose again.")

#test-commit2

if __name__ == '__main__':
    main()







