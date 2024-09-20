from bank import TitleBank


class SavingsAccount(TitleBank):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def interest_applied(self):
        interest = self.current_balance * (self.interest_rate / 100)
        self.current_balance += interest
        print("Interest: $" + str(interest) + " New Balance: $" + str(self.current_balance))

    def print_customer_information(self):
        super().print_customer_information()
        print("Account Number:", self._account_number,
              "\nInterest Rate: " + str(self.interest_rate) + "%")


class CheckingAccount(TitleBank):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount > 0:
            if amount > self.transfer_limit:
                print("Transfer denied. Exceeds limit.")
            elif (self.current_balance - amount) >= self.minimum_balance:
                self.current_balance -= amount
                print("Transferred: $" + str(amount) + " New Balance: $" + str(self.current_balance))
            else:
                print("Transfer denied.")
        else:
            print("Invalid transfer amount.")

    def print_customer_information(self):
        super().print_customer_information()
        print("Account Number:", self._account_number,
              "\nTransfer Limit:", self.transfer_limit)

