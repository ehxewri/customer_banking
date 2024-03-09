# import Accounts and Account class from Account
from Account import Account
# import addional packages to support formating
from rich.console import Console
console = Console()
console.clear()

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
        my_account.calc_accrued()
        # update the account balance
        my_account.update_balance()
        # print (f'\nYour {account} account interest at maturity for {length_of_deposit} months is {interest_earned}')
        my_account.print_interest_accrued()
        # print (f'\nYour new {account} balance will be {updated_balance}\n')
        my_account.print_updated_balance()

if __name__ == "__main__":
    # set the account list to the accounts you ant to start. I added an extra one. the idea is to have everything passed to the main function
    account_list=['Savings','CD','Checking']
    # Call the main function.
    main(account_list)