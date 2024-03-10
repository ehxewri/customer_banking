import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
from CustValInput import NumDotDD, IntValidator
from prompt_toolkit import prompt
# from prompt_toolkit.validation import Validator, ValidationError
# import re

# Create a Account class with methods   
class Account:
    # this methood initializes the instance
    def __init__(self,account):
        self.account            = account 
        self.balance            = 0
        self.interest_rate      = 0
        self.length_of_deposit  = 0
        self.interest_earned    = 0
    # This methood sets the balance of the account.
    def get_account_info(self):
        self.balance            = prompt(f'\nPlease enter your initial {self.account} account balanace : $ ',validator=NumDotDD())
        self.interest_rate      = prompt(f'Please enter your {self.account} account interest rate : % ',validator=NumDotDD())
        self.length_of_deposit  = int(input(f'Please enter your {self.account} account deposit duration in months : '))
    # The methood sets the interest gained for the account.
    def calc_accrued(self):
        """Sets the interest gained for the the account"""
        self.interest_earned    = (self.balance*(self.interest_rate/100/12)*self.length_of_deposit)
    # The methood updates the balance for the account.
    def update_balance(self):
        """Sets the balance for the for the account"""
        self.balance            = self.balance + self.interest_earned
    # The methood prints the interest accrued for the account.
    def print_interest_accrued(self):
        print (f'\nYour {self.account} account interest at maturity for {self.length_of_deposit} months is {locale.currency(self.interest_earned)}')
    # The method prints the updated balance for the account.
    def print_updated_balance(self):
        print (f'Your new {self.account} balance will be {locale.currency(self.balance)}\n')
