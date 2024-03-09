""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest_earned):
        self.balance = balance
        self.interest_earned = interest_earned

    # This method sets the balance of the account.
    def set_balance(self, balance, interest_earned):
        """Sets the balance for the for the account"""
        balance = balance + interest_earned
        return balance

    # The method sets the interest gained for the account.
    def set_interest(self, balance,interest_rate,length_of_deposit):
        """Sets the interest gained for the the account"""
        interest_earned = (balance*(interest_rate/100/12)*length_of_deposit)
        return interest_earned

class Account_types:
    def __init__(self,account_types):
        self.account_types = account_types

    def accounts(self):
        self.account_types = ('Saving','CD')
        return self.account_types