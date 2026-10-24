balance = 0
transactions = []
pin = "1234"

def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ${amount:.2f}")
        print(f"Amount deposited successfully. Current balance: ${balance:.2f}")
    else:
        print("Enter a valid amount.")

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Enter a valid amount.")
    elif amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn: ${amount:.2f}")
        print(f"Amount withdrawn successfully. Current balance: ${balance:.2f}")
    else:
        print("Insufficient funds.")

def check_balance():
    
    print(f"Current balance: ${balance:.2f}")

def transaction_history():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\nTransaction History:")
        for transaction in transactions:
            print(transaction)

def transfer_money():
    global balance

    account = input("Enter receiver account number: ")
    amount = float(input("Enter amount to transfer: "))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount <= balance:
        balance -= amount
        transactions.append(f"Transferred ${amount:.2f} to Account {account}")
        print(f"${amount:.2f} transferred successfully.")
        print(f"Current balance: ${balance:.2f}")
    else:
        print("Insufficient funds.")

def calculate_interest():
    global balance

    rate = float(input("Enter annual interest rate (%): "))
    years = float(input("Enter number of years: "))

    interest = balance * rate * years / 100
    final_balance = balance + interest

    print(f"Interest earned: ${interest:.2f}")
    print(f"Balance after interest: ${final_balance:.2f}")

def change_pin():
    global pin
    old_pin = input("Enter current PIN: ")

    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        pin = new_pin
        print("PIN changed successfully.")
    else:
        print("Incorrect PIN.")

def banking_system():
    global balance

    print("Welcome to the Banking Program")

    entered_pin = input("Enter your PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("\n===== BANKING MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Transfer Money")
        print("6. Calculate Interest")
        print("7. Change PIN")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            deposit()

        elif choice == "2":
            withdraw()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            transaction_history()

        elif choice == "5":
            transfer_money()

        elif choice == "6":
            calculate_interest()

        elif choice == "7":
            change_pin()

        elif choice == "8":
            print("Thank you for using the Banking Program!")
            break

        else:
            print("Invalid choice. Please try again.")

banking_system()