""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance, interest_earned):
        """Sets the balance for the for the account"""
        self.balance = balance + interest_earned
        return self.balance

    # The method sets the interest gained for the account.
    def set_interest(self, balance,interest_rate,months):
        """Sets the interest gained for the the account"""
        self.interest = (balance*(interest_rate/100/12)*months)
        return self.interest

class account_type:

    def __init__(self,account_type):
        self.account_type = account_type
