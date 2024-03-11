import locale
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from Cust_val_input import IntValidator, CurrencyValidator,InterestRateValidator
from rich.console import Console

# Set locale to use in currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
console =Console()
style_greenbold = Style([('prompt', 'fg:ansigreen bold')])
style_yellowbold = Style([('prompt', 'fg:ansiyellow bold')])
style_bluebold = Style([('prompt', 'fg:ansiblue bold')])

class Account:
    # Represents a bank account with operations to manage account details.

    def __init__(self, account_type):
        """Initialize the account with default values."""
        self.account_type = account_type
        self.balance = 0.0
        self.interest_rate = 0.0
        self.deposit_term = 0
        self.interest_earned = 0.0
        self.accrued_interest_earned = 0.0

    def get_account_info(self):
        """Gather account details from user input."""
        self.balance = float(prompt(f'\nPlease enter your initial {self.account_type} account balance: $ ',style=style_greenbold, validator=CurrencyValidator()))
        self.interest_rate = float(prompt(f'Please enter your {self.account_type} account interest rate (%): ',style=style_yellowbold, validator=InterestRateValidator()))
        self.deposit_term = int(prompt(f'Please enter your {self.account_type} account deposit duration (months): ', rprompt='are you sure?', style=style_bluebold, bottom_toolbar='penalties for early withdraw', validator=IntValidator()))

    def calculate_interest(self):
        """Calculate and update interest earned based on account details.
        accrued interest = deposit amount*interest rate/(12)**12*term in months/12
        
        """
        self.interest_earned = self.balance * (self.interest_rate / 100 / 12) * self.deposit_term
        self.accrued_interest_earned = self.balance * (1 + (self.interest_rate/100/12))**(12*(self.deposit_term/12))-self.balance
        
    def update_balance(self):
        """Update the account balance to include earned interest."""
        self.balance += self.accrued_interest_earned

    def display_interest_earned(self):
        """Print the interest earned over the deposit term."""
        console.print(f'\nYour {self.account_type} account interest for {self.deposit_term} months is {locale.currency(self.interest_earned, symbol=True, grouping=True)}',style='blue')

    def display_accrual_balance(self):
        """Print the updated account balance."""
        console.print(f'\nWith interest compounded monthly, your new {self.account_type} interest is {locale.currency(self.accrued_interest_earned, symbol=True, grouping=True)}',style='blue')

    def display_updated_balance(self):
        """Print the updated account balance."""
        console.print(f'Your new {self.account_type} balance will be {locale.currency(self.balance, symbol=True, grouping=True)}\n',style='blue')
        
# Example usage
if __name__ == "__main__":
    account = Account("Savings")
    account.get_account_info()
    account.calculate_interest()
    account.update_balance()
    account.display_interest_earned()
    account.display_accrual_balance()
    account.display_updated_balance()