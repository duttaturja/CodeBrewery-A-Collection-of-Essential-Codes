class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private variable (encapsulation)

    # Getter method to access the private balance
    def get_balance(self):
        return self.__balance

    # Setter method to modify the private balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Usage
account = BankAccount("John Doe", 1000)

# Accessing balance using getter method
print(f"Initial Balance: {account.get_balance()}")

# Depositing money
account.deposit(500)
print(f"Balance after deposit: {account.get_balance()}")

# Withdrawing money
account.withdraw(300)
print(f"Balance after withdrawal: {account.get_balance()}")

# Trying to access the private balance directly (will result in error)
# print(account.__balance)  # Uncommenting this will cause an AttributeError
