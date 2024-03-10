# import Accounts and Account class from Account
from Account import Account

# import addional packages to support formating
from rich.console import Console

import argparse
# Create Clear Console
console = Console()
console.clear()
# set currency 
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# Create the parser
parser = argparse.ArgumentParser(description='add account names\n one space between names\nno spaces in the name\nno special characters')
# Add an argument to collect keywords into a list
# nargs='*' tells argparse to collect all positional arguments in a list
parser.add_argument('keywords', nargs='*', help='List of keywords')
# Parse the arguments
args = parser.parse_args()
# args.keywords will contain the list of keywords
# Define the main function
def main(account_list):
    # instanciate my_account from Accounts class    
    """ for each account type
        Initialize the account
        get account info
        calculate the intereste accrued
        calculat the new balance
        print interest accrued and new balance
    """ 
    for account in account_list:
        # instanciate account from account class 
        my_account=Account(account)
        # Prompt the user to set the savings balance, interest rate, and months for the savings account.
        my_account.get_account_info()
        # Calculate Interest accrued
        console.clear() 
        my_account.calc_accrued()
        # update the account balance
        my_account.update_balance()
        # print (f'\nYour {account} account interest at maturity for {length_of_deposit} months is {interest_earned}')
        my_account.print_interest_accrued()
        # print (f'\nYour new {account} balance will be {updated_balance}\n')
        my_account.print_updated_balance()

if __name__ == "__main__":
    # set the account list to the accounts you want to start. 
    # If accounts are not passed when the program is started it will default to savigns and cd
    if len(args.keywords) > 0:
        account_list=args.keywords
    else: 
        account_list=['Savings','CD']
    # Call the main function.
    main(account_list)