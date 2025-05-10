import os

DATA_FILE = 'accounts.txt'

def load_accounts():
    accounts = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    account_number, username, NIC_number, password, balance = parts
                    accounts[username] = {
                        'account_number': account_number,
                        'NIC_number': NIC_number,
                        'password': password,
                        'balance': float(balance)
                    }
    return accounts

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        for username, info in accounts.items():
            file.write(f"{info['account_number']},{username},{info['NIC_number']},{info['password']},{info['balance']}\n")

def generate_account_number(accounts):
    existing_numbers = [int(info['account_number']) for info in accounts.values()]
    return str(max(existing_numbers, default=100000) + 1)

def create_account(accounts):
    NIC_number = input("Enter your NIC number: ").strip()
    if any(info['NIC_number'] == NIC_number for info in accounts.values()):
        print("NIC number already exists.")
        return

    username = input("Enter new username: ").strip()
    if username in accounts:
        print("Username already exists.")
        return

    password = input("Enter password: ").strip()
    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance. Account not created.")
        return

    account_number = generate_account_number(accounts)
    accounts[username] = {
        'account_number': account_number,
        'password': password,
        'balance': balance,
        'NIC_number': NIC_number
    }

    print(f"Account created successfully! Your account number is: {account_number}")

def user_login(accounts):
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = accounts.get(username)
    if user and user['password'] == password:
        print(f"Welcome {username}!")
        user_menu(accounts, username)
    else:
        print("Invalid username or password.")

def user_menu(accounts, username):
    while True:
        print(f"\n--- {username.upper()}'s ACCOUNT ---")
        print(f"Account Number: {accounts[username]['account_number']}")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer money")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance(accounts, username)
        elif choice == '2':
            deposit(accounts, username)
        elif choice == '3':
            withdraw(accounts, username)
        elif choice == '4':
            transfer_money(accounts, username)
        elif choice == '5':
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

def transfer_money(accounts, sender):
    receiver = input("Enter recipient username: ").strip()
    if receiver not in accounts:
        print("Recipient account not found.")
        return
    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > accounts[sender]['balance']:
            print("Insufficient funds.")
        else:
            accounts[sender]['balance'] -= amount
            accounts[receiver]['balance'] += amount
            print(f"${amount:.2f} transferred to {receiver}.")
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

if __name__ == '__main__':
    main()