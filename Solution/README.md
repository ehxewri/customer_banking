# Module 3 Challenge

I really tried to stick to the assignment. I was so bored I fell asleep twice. Running `customer_banking.py`, you'll see it looks like the requirements are met. I just changed where things are done and how. I added input validation and output formatting to ensure the input was good and the output was readable. If the code is not understood the way I have it, I missed the point of readable code.
## Fun with Banking

This exercise let me dive deeper into a few new concepts I've wanted to understand better:

- Starting programs and passing arguments
- Validating input to prevent bad input from causing havoc
- Understanding when to use standalone functions and when to use methods in a class
- Adding a test for the account that verified the basic operation of all methods

This should help in navigating the simple program. Enjoy
-   - Try `Customer_banking.py -help`.

## Customer Banking System 

`customer_banking.py`

For each account:
- Accept input from the user for account balance, interest rate, and term length.
- Calculate the interest accrued.
- Update the balance.
- Print the interest accrued.
- Print the updated balance.

The exercise is to write a module that lets a user calculate interest and the new balance of accounts. The module needs to accept `current_balance`, `interest rate`, `deposit term`. The output will be interest accumulated and new balance at the end of the deposit term.

## Requirements

- Create the ~~Savings Account Function~~ (35 points)
    - All functions are methods in the Account class.

    - The Account class from the `Accounts.py` file is imported. (4 points)
        - `customer_banking "from Account import Account"`

    - In the ~~create_savings_account function~~ in the main function, an instance of the Account class is created ~~and the balance and interest parameters~~ account name is passed to the Account class. (6 points)

    - The interest earned is calculated and assigned to a variable. (4 points)
        - `calculate_interest` in the Account Class.

    - The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
        - `update_balance` in the Account Class.

    - The updated balance is passed to the set balance method using the instance of the Account class. (6 points)
        - `update_balance` in the Account Class.

    - The interest earned is passed to the set balance method using the instance of the Account class. (6 points)
        - `calculate_interest` in the Account Class.

    - The updated balance and interest earned are returned by the function. (5 points)
        - This would be simple but not required. 
        - `return (Updated_balance, interest_earned)`

- ~~Create the CD Account Function~~ (35 points) The program is now a loop of accounts. 

### Create the Main Function (30 points)

- The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)
    - Moved to Account class method `get_account_info`.

- Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousands. (6 points)
    - Moved to Account class `display_interest_earned` and `display_updated_balance`.

- The user is prompted to set the savings balance, interest rate, and months for the CD account. (8 points)
    - Moved to `get_account_info`.

- Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousands. (6 points)
    - Used locale.currency

- The main function is called to run the program. (2 points)
  
