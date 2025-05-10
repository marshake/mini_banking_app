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
