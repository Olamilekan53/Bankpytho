class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"{self.owner}'s account balance: ${self.balance:.2f}")

def main():
    # Accepting user fullname
    fullname = input("Enter your full name: ")
    # Creating a bank account for the user
    user_account = BankAccount(fullname)
    
    while True:
        print("\nBank Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            user_account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            user_account.withdraw(amount)
        elif choice == '3':
            user_account.display_balance()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
