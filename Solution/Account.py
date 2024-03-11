import locale
from prompt_toolkit import prompt
from Cust_val_input import IntValidator, CurrencyValidator,InterestRateValidator

# Set locale to use in currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class Account:
    # Represents a bank account with operations to manage account details.

    def __init__(self, account_type):
        """Initialize the account with default values."""
        self.account_type = account_type
        self.balance = 0.0
        self.interest_rate = 0.0
        self.deposit_term = 0
        self.interest_earned = 0.0

    def get_account_info(self):
        """Gather account details from user input."""
        self.balance = float(prompt(f'\nPlease enter your initial {self.account_type} account balance: $ ', validator=CurrencyValidator()))
        self.interest_rate = float(prompt(f'Please enter your {self.account_type} account interest rate (%): ', validator=InterestRateValidator()))
        self.deposit_term = int(prompt(f'Please enter your {self.account_type} account deposit duration (months): ', validator=IntValidator()))

    def calculate_interest(self):
        """Calculate and update interest earned based on account details."""
        self.interest_earned = self.balance * (self.interest_rate / 100 / 12) * self.deposit_term

    def update_balance(self):
        """Update the account balance to include earned interest."""
        self.balance += self.interest_earned

    def display_interest_earned(self):
        """Print the interest earned over the deposit term."""
        print(f'\nYour {self.account_type} account interest for {self.deposit_term} months is {locale.currency(self.interest_earned, symbol=True, grouping=True)}')

    def display_updated_balance(self):
        """Print the updated account balance."""
        print(f'Your new {self.account_type} balance will be {locale.currency(self.balance, symbol=True, grouping=True)}\n')

# Example usage
if __name__ == "__main__":
    account = Account("Savings")
    account.get_account_info()
    account.calculate_interest()
    account.update_balance()
    account.display_interest_earned()
    account.display_updated_balance()