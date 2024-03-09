# import Accounts and Account class from Account
from Account import Accounts, Account
# import addional packages to support formating
from rich.console import Console
console = Console()
console.clear()
# Define the main function
def main(account_list):
    # instanciate my_account from Accounts class
    my_accounts=Accounts(account_list)    
    """ for each account type
        Initialize the account
        calculate the intereste accrued
        calculat the new balance
        print interest accrued and new balance
    """ 
    for account in my_accounts.accounts:
        # instanciate account from account class 
        my_account=Account(account,0,0,0,0)
        # Prompt the user to set the savings balance, interest rate, and months for the savings account.
        my_account.get_account_info()
        # Calculate Interest accrued 
        my_account.calc_accrual()
        # update the account balance
        my_account.update_balance()
        # print (f'\nYour {account} account interest at maturity for {length_of_deposit} months is {interest_earned}')
        my_account.print_interest_accrued()
        # print (f'\nYour new {account} balance will be {updated_balance}\n')
        my_account.print_updated_balance()

if __name__ == "__main__":
    account_list=['Savings','CD']
    # Call the main function.
    main(account_list)