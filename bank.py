class TitleBank:
    # Class attribute
    bank_name = 'Title Bank'

    # Instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected
        self.__routing_number = routing_number  # Private

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
        routing_mask = '*' * len(str(self.__routing_number))

        print("Bank:", TitleBank.bank_name,
              "\nCustomer Name:", self.customer_name,
              "\nCurrent Balance: $" + str(self.current_balance) +
              "\nMinimum Balance: $" + str(self.minimum_balance) +
              "\nRouting Number: ", routing_mask)

    def get_routing(self):
        return self.__routing_number

    def get_account(self):
        return self._account_number

    def set_routing(self, new_routing_num):
        self.__routing_number = new_routing_num

    def set_account(self, new_account_num):
        self._account_number = new_account_num

