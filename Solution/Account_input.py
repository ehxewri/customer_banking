def account_input(account):
    starting_balance    = int(input(f'\nPlease enter your initial {account} account balanace : '))
    interest_rate       = int(input(f'Please enter your {account} account interest rate : '))
    duration_months     = int(input(f'Please enter your {account} account deposit duration in months : '))
    return (starting_balance, interest_rate, duration_months)