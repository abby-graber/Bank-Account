# Abby Graber ITSC-3155 09/19/2024

class TitleBank:
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
        print("Bank:", TitleBank.bank_name,
              "\nCustomer Name:", self.customer_name,
              "\nCurrent Balance: $" + str(self.current_balance) +
              "\nMinimum Balance: $" + str(self.minimum_balance))


class SavingsAccount(TitleBank):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def interest_applied(self):
        interest = self.current_balance * (self.interest_rate / 100)
        self.current_balance += interest
        print("Interest: $" + str(interest) + " New Balance: $" + str(self.current_balance))

    def print_customer_information(self):
        super().print_customer_information()
        print("Interest Rate: " + str(self.interest_rate) + "%")


class CheckingAccount(TitleBank):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount > 0:
            if amount > self.transfer_limit:
                print("Transfer denied.")
            elif (self.current_balance - amount) >= self.minimum_balance:
                self.current_balance -= amount
                print("Transferred: $" + str(amount) + " New Balance: $" + str(self.current_balance))
            else:
                print("Transfer denied.")
        else:
            print("Invalid transfer amount.")

    def print_customer_information(self):
        super().print_customer_information()
        print("Transfer Limit:", self.transfer_limit)


# Test instances
c1 = TitleBank("Abby", 1000, 500)
c1.deposit(300)
c1.withdraw(500)
c1.print_customer_information()

print()

c2 = TitleBank("Gojo", 10000, 1000)
c2.deposit(5000)
c2.withdraw(1000)
c2.print_customer_information()

print()

c3 = SavingsAccount("Sukuna", 3000, 900, 2.5)  # 2.5% interest rate
c3.deposit(690)
c3.withdraw(1000)
c3.interest_applied()  # Apply interest to the balance
c3.print_customer_information()

print()

c4 = CheckingAccount("Geto", 4000, 650, 1000)  # $1000 transfer limit
c4.deposit(2000)
c4.withdraw(300)
c4.transfer(1500)
c4.transfer(900)
c4.print_customer_information()
