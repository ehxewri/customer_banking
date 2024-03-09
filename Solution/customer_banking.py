# Import the account_Accrual and account_input from Account_action
from Account_actions import account_input, account_accrual
from Account import Account_types
# import addional packages to support formating
from rich.console import Console
console = Console()
console.clear()
# Define the main function
def main():
    """this funtiongets the account types for savings and cd (uses account type class)
        for each account 
            get account_input
            caculate account accrual and new balance (uses accout class- think of better descriptive name)
            print account accrual and new balance
    """ 
    my_accounts=Account_types()

    print (my_accounts) 

    for account in my_accounts:
        # Prompt the user to set the savings balance, interest rate, and months for the savings account.
        starting_balance, interest_rate, length_of_deposit = account_input(account)
        # Call the create_savings_account function and pass the variables from the user.
        updated_balance, interest_earned = account_accrual(starting_balance, interest_rate, length_of_deposit)
        print (f'\nYour {account} account interest at maturity for {length_of_deposit} months is {interest_earned}')
        print (f'\nYour new {account} balance will be {updated_balance}\n')

if __name__ == "__main__":
    # Call the main function.
    main()