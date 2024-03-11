import argparse
from Account import Account
from rich.console import Console
from My_tools import pause, clear

# Initialize the console for output and clear any previous output
console = Console()
# console.clear()

def create_argument_parser():
    """
    Creates and configures the argument parser for command line argument
    This is not part of the assignment
    it permits the program to accept an account list and process it in place of the default
    If you do not pass account names it will use the default "Savings, CD" as the assignment requires
    """
    parser = argparse.ArgumentParser(description='Process account names. Use one space between names. No spaces within a name. No special characters.')
    parser.add_argument('accounts', nargs='*', default=['Savings', 'CD'], help='List of account names')
    return parser

def process_accounts(account_list):
    """
    Processes each account in the provided list by getting account info, calculating interest, and updating balance.
    """
    for account_name in account_list:
        # Clear the console before displaying account updates for readability
        clear()
        console.print(f"Create {account_name} Account : ", style="blue")
        account = Account(account_name)
        account.get_account_info()
        account.calculate_interest()
        account.update_balance()
        account.display_interest_earned()
        account.display_updated_balance()
        pause('Press enter to continue')

def main():
    """
    Main function to handle the workflow of processing accounts.
    """
    parser = create_argument_parser()
    args = parser.parse_args()
    process_accounts(args.accounts)
    pause('Press enter to exit')
    clear()
if __name__ == "__main__":
    main()