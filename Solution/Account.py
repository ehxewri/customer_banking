""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self,account, balance, interest_rate,length_of_deposit,interest_earned):
        self.account            = account 
        self.balance            = balance
        self.interest_rate      = interest_rate
        self.length_of_deposit  = length_of_deposit
        self.interest_earned    = interest_earned

    # This method sets the balance of the account.
    def get_account_info(self):
        self.balance            = float(input(f'\nPlease enter your initial {self.account} account balanace : '))
        self.interest_rate      = float(input(f'Please enter your {self.account} account interest rate : '))
        self.length_of_deposit  = int(input(f'Please enter your {self.account} account deposit duration in months : '))

    # The method sets the interest gained for the account.
    def calc_accrual(self):
        """Sets the interest gained for the the account"""
        self.interest_earned    = (self.balance*(self.interest_rate/100/12)*self.length_of_deposit)

    def update_balance(self):
        """Sets the balance for the for the account"""
        self.balance            = self.balance + self.interest_earned

    def print_interest_accrued(self):
        print (f'\nYour {self.account} account interest at maturity for {self.length_of_deposit} months is {self.interest_earned}')
    def print_updated_balance(self):
        print (f'Your new {self.account} balance will be {self.balance}\n')

class Accounts:
    def __init__(self,accounts):
        self.accounts = accounts