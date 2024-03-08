class account_input:

    def __init__(self,account_type):
        self.account_type = account_type

    def get_input(self,account_type)
        balance = float(input(f'What is your {self.account_type} account balance? '))
        interest = float(input(f'What is the APR for the {self.account_type} account? '))
        maturity = int(input(f'What is the length of months you want to calculate the interest gained on the {self.account_type} account? '))