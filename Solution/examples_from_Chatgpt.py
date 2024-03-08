'''
The updated Python code defines a class `CDAccount` that represents a Certificate of Deposit (CD) 
account and includes functionality to calculate the future value of the CD account considering compound interest. 
The `create_cd_account` function is used to create instances of `CDAccount` with specified attributes. 
Here's a breakdown of what each part does:

1. **`CDAccount` Class Definition**:
   - **Initialization (`__init__` method)**: Constructs an instance of the `CDAccount` class with the account holder's name,
    the initial deposit amount, the annual interest rate (as a percentage), the term length in months, 
    and the frequency of interest compounding per year.
   - **Compound Interest Calculation 
    (`calculate_compounded_interest` method)**: 
    Calculates the future value of the CD account after interest has been compounded over the term of the deposit. 
    The calculation is based on the formula for compound interest, considering the deposit amount, 
    the annual interest rate (converted to a decimal), the length of the term in years (calculated from months), 
    and the compounding frequency.
   - **String Representation (`__str__` method)**: Provides a human-readable string representation of the CD account, 
    including the account holder's name, deposit amount, annual interest rate, term length, compounding frequency, 
    and the calculated future value of the account.

2. **`create_cd_account` Function**:
    - This function serves as a factory to create `CDAccount` instances. 
    It takes the same parameters required by the `CDAccount` constructor 
    (`holder_name`, `deposit_amount`, `annual_interest_rate`, `term_length_months`, `compound_frequency`) 
    and returns a new instance of `CDAccount`.

3. **Example Usage**:
    - The example creates a CD account for "John Doe" with a $10,000 deposit, a 2.5% annual interest rate, 
    a 12-month term, and quarterly compounding (4 times a year). 
    It then prints the details of this account, including the future value after interest compounding.

The key feature added is the calculation of compounded interest, which significantly impacts the future value of the CD account. Compounding interest means that interest earned accrues not only on the initial principal but also on the accumulated interest over time. The frequency of compounding (in this case, quarterly) affects how much interest is earned: more frequent compounding generally leads to higher returns over the same term. 

By running this code, users can understand how different interest rates, compounding frequencies, and term lengths affect the potential growth of their CD investments.
'''
class CDAccount:
    def __init__(self, holder_name, deposit_amount, annual_interest_rate, term_length_months, compound_frequency):
        self.holder_name = holder_name
        self.deposit_amount = deposit_amount
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.term_length_months = term_length_months
        self.compound_frequency = compound_frequency  # How many times per year interest is compounded

    def calculate_compounded_interest(self):
        """
        Calculates the future value of the CD account after applying compounded interest.

        Returns:
        - float: The future value of the CD account.
        """
        periods = self.compound_frequency * (self.term_length_months / 12)
        amount = self.deposit_amount * (1 + self.annual_interest_rate / self.compound_frequency) ** periods
        return amount

    def __str__(self):
        future_value = self.calculate_compounded_interest()
        return (f"CD Account Holder: {self.holder_name}\n"
                f"Deposit Amount: ${self.deposit_amount}\n"
                f"Annual Interest Rate: {self.annual_interest_rate * 100}%\n"
                f"Term Length: {self.term_length_months} months\n"
                f"Compound Frequency: {self.compound_frequency} times per year\n"
                f"Future Value: ${future_value:.2f}")

def create_cd_account(holder_name, deposit_amount, annual_interest_rate, term_length_months, compound_frequency):
    """
    Creates and returns a CDAccount instance with the provided details.

    Parameters:
    - holder_name (str): The name of the account holder.
    - deposit_amount (float): The amount of money deposited in the account.
    - annual_interest_rate (float): The annual interest rate of the CD in percentage.
    - term_length_months (int): The length of the CD term in months.
    - compound_frequency (int): The number of times interest is compounded per year.

    Returns:
    - CDAccount: An instance of the CDAccount class.
    """
    new_cd_account = CDAccount(holder_name, deposit_amount, annual_interest_rate, term_length_months, compound_frequency)
    return new_cd_account

# Example usage
cd_account = create_cd_account("John Doe", 10000, 2.5, 12, 4)  # Quarterly compounding
print(cd_account)
