# Abby Graber ITSC-3155 09/19/2024

from bank import TitleBank
from accounts import SavingsAccount, CheckingAccount

''' User Story: user opens savings account and then withdrawals an amount from current balance'''
user = SavingsAccount("Zim", 234000, 15000, 1.5,
                      "ACC000", "0248284")
user.interest_applied()
user.withdraw(6000)
user.print_customer_information()

print("\n")

# Test instances
c1 = TitleBank("Abby", 1000, 500,
               "ACC123", "9876543")
c1.deposit(300)
c1.withdraw(500)
c1.print_customer_information()

print()

c2 = TitleBank("Gojo", 10000, 1000,
               "ACC987", "2648562")
c2.deposit(5000)
c2.withdraw(1000)
c2.print_customer_information()

print()

c3 = SavingsAccount("Sukuna", 3000, 900, 2.5,
                    "ACC634", "7342910")
c3.deposit(690)
c3.withdraw(1000)
c3.interest_applied()  # Apply interest to the balance
c3.print_customer_information()

print()

c4 = SavingsAccount("Megumi", 200, 100, 3.3,
                    "ACC911", "8253478")
c4.deposit(10000)
c4.withdraw(200)
c4.interest_applied()
c4.print_customer_information()

print()

c5 = CheckingAccount("Geto", 4000, 650, 1000,
                     "ACC834", "2094762")
c5.deposit(2000)
c5.withdraw(300)
c5.transfer(900)
c5.print_customer_information()

print()

c6 = CheckingAccount("Yuuji", 3500, 250, 1500,
                     "ACC444", "3840284")
c6.deposit(1)
c6.withdraw(3499)
c6.transfer(2000)
c6.print_customer_information()
