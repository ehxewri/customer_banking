from Account import Account

# get starting balance, interest rate and length_of_deposit
def account_input(account):
    starting_balance    = float(input(f'\nPlease enter your initial {account} account balanace : '))
    interest_rate       = float(input(f'Please enter your {account} account interest rate : '))
    length_of_deposit   = int(input(f'Please enter your {account} account deposit duration in months : '))
    return (starting_balance, interest_rate, length_of_deposit)

# Define a function for the accruing interest on an account
def account_accrual(starting_balance, interest_rate, length_of_deposit):
    """initialize an account, calculates interest earned, and updates the account balance.

    Args:
        starting_balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        lenght_of Deposit (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    my_account = Account(starting_balance,0)

    # Calculate interest earned0
    my_account.set_interest(my_account.balance,interest_rate,length_of_deposit)

    # Update the savings account balance by adding the interest earned
    my_account.set_balance(my_account.balance,my_account.interest_earned)

    # Return the updated balance and interest earned.
    return my_account.balance, my_account.interest_earned 
