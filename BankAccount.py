# Abby Graber ITSC-3155 09/03/2024

class TitleBank():
    # Class attribute
    bank_name = 'Title Bank'

    # Instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:  # Check for positive amount
            self.current_balance += amount  # Add deposited amount
            print("Deposited: $" + str(amount) + " New Balance: $" + str(self.current_balance))
        else:  # Deposit is not changed if amount is not a positive number
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0:  # Check for a positive amount
            if (self.current_balance - amount) >= self.minimum_balance:
                # Subtract withdrawal amount after verifying the balance won't go below the minimum
                self.current_balance -= amount
                print("Withdrawal: $" + str(amount) + " New Balance: $" + str(self.current_balance))
            else:  # Validate withdrawal amount
                print("Withdrawal denied. Balance cannot go below approved minimum.")
        else:  # Withdraw is not changed if amount is not a positive number
            print("Withdrawal amount must be positive.")

    # Print Customer Information method
    def print_customer_information(self):
        print("Bank: ", TitleBank.bank_name,
              "\nCustomer Name:", self.customer_name,
              "\nCurrent Balance: $" + str(self.current_balance) +
              "\nMinimum Balance: $" + str(self.minimum_balance))

# Test instances
c1 = TitleBank("Abby", 1000, 500)
c1.deposit(300)
c1.withdraw(500)
c1.print_customer_information()

c2 = TitleBank("Gojo", 10000, 1000)
c2.deposit(5000)
c2.withdraw(1000)
c2.print_customer_information()
