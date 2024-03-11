from prompt_toolkit.validation import Validator, ValidationError
import re

class CurrencyValidator(Validator):
    """
    Validates that the input is a valid currency amount with up to two decimal places.
    """
    def validate(self, document):
        text = document.text
        if not re.match(r'^\d+(\.\d{1,2})?$', text):
            raise ValidationError(
                message="Please enter a valid currency amount (up to two decimal places)",
                cursor_position=len(text)
            )

class InterestRateValidator(Validator):
    """
    Validates that the input is a valid interest rate with up to three decimal places.
    """
    def validate(self, document):
        text = document.text
        if not re.match(r'^\d+(\.\d{1,3})?$', text):
            raise ValidationError(
                message="Please enter a valid interest rate (up to three decimal places)",
                cursor_position=len(text)
            )

class FloatValidator(Validator):
    """
    Validates that the input is a valid float.
    """
    def validate(self, document):
        text = document.text
        try:
            float(text)
        except ValueError:
            raise ValidationError(
                message="This input is not a valid number",
                cursor_position=len(text)
            )

class IntValidator(Validator):
    """
    Validates that the input is a valid integer.
    """
    def validate(self, document):
        text = document.text
        try:
            int(text)
        except ValueError:
            raise ValidationError(
                message="This input is not a valid integer",
                cursor_position=len(text)
            )

class EnterValidator(Validator):
    """
    Checks if the enter key was pressed, assuming empty input is intended to trigger this.
    """
    def validate(self, document):
        text = document.text
        if text:
            raise ValidationError(
                message="Press enter to continue",
                cursor_position=len(text)
            )