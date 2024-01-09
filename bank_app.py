class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


def create_account():
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_holder, initial_balance)


def display_balance(account):
    print(f"Current balance: {account.check_balance()}")


def perform_deposit(account):
    amount = float(input("Enter deposit amount: "))
    if account.deposit(amount):
        print("Deposit successful.")
    else:
        print("Invalid deposit amount.")


def perform_withdrawal(account):
    amount = float(input("Enter withdrawal amount: "))
    if account.withdraw(amount):
        print("Withdrawal successful.")
    else:
        print("Invalid withdrawal amount or insufficient funds.")


if __name__ == "__main__":
    # Create a new account
    account1 = create_account()

    while True:
        print("\nOptions:")
        print("1. Display Balance")
        print("2. Make a Deposit")
        print("3. Make a Withdrawal")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_balance(account1)
        elif choice == '2':
            perform_deposit(account1)
        elif choice == '3':
            perform_withdrawal(account1)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
