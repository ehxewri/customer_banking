# Python Program Pseudocode Outline

1. **Start**

2. **Initialize necessary variables**
    - This could be counters, accumulators, or any specific data type required for the task.

3. **Define functions (if any)**
    - **Function to perform calculations**
        1. Take inputs (parameters).
        2. Perform calculation.
        3. Return result.
    
    - **Function to process input/output**
        1. Read user input.
        2. Validate or transform input if necessary.
        3. Display outputs or messages to the user.

4. **Main Program Flow**
    - **Read or gather input**
        - Use input function for text or other methods for different types of input.
    
    - **Process the input (could involve calling a function)**
        - Pass input to the calculation function or directly perform operations.
    
    - **Output the results**
        - Print the results or output to a file or database as required.

5. **Error handling (Optional)**
    - Include try-except blocks to handle exceptions or errors gracefully.

6. **End**


## Module 3 Challenge


* Due Monday by 11:59pm 
* Points 100 
* Submit  website url

## Description 
You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

* Will we compount the interest?
* what will the compound interval be? 
    * daily
    * weekly
    * monthly
    * quarterly
    * yearly


## Before You Begin
Before starting the assignment, be sure to complete the following steps:

* Create a new repository for this project called customer_banking. 
* Clone the new repository to your computer.
* Inside your local Git repository, add the starter files from your file [downloads](https://git.bootcampcontent.com/Southern-Methodist-University/SMU-VIRT-AI-PT-02-2024-U-LOLC/-/tree/main/Homework/03-Python-Programming-2/Starter_Code?ref_type=heads). 
    * Accounts.py
    * savings_account.py
    * cd_account.py
    * customer_banking.py
* Push these changes to GitHub or GitLab.

## Challenge Instructions
* Accounts.py 
    * file contains the Account class with methods to set the balance and interest.

* In the savings_account.py file 35 points
    * import the Account class 
    * create a create_savings_account function that will create a savings account instance 
    * calculate the interest earned based on user input
    * update the account balance with the earned interest
    * return the updated balance and interest earned.

* In the cd_account.py file 35 points
    * import the Account class
    * create a create_cd_account function that will create a CD account instance
    * calculate the interest earned based on user input
    * update the account balance with the earned interest
    * return the updated balance and interest earned.

* In the customer_banking.py file 30 points
    * Import the create_cd_account and create_savings_account functions from the appropriate files
    * create a main function that prompts the user to enter the savings and CD account details
    * call the corresponding functions to calculate the interest earned and update the balances
    * display the results.

Create the Savings Account Function
Open the savings_account.py file, and do the following:

Imports the Account class from the Accounts.py file.

In the create_savings_account function do the following:

Create an instance of the Account class and pass in the balance and interest parameters.

Calculate interest earned.