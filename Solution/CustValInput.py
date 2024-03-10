from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
import re
class NumDotDD(Validator):
# this requires the input to be a with only two decimal places
    def validate(self, document):
        text = document.text
        # Regular expression to match a valid currency format with up to two decimal places
        if text:
            if not re.match(r'^\d+(\.\d{1,2})?$', text):
                # If the input doesn't match the pattern, raise a validation error
                raise ValidationError(
                    message="Please enter a valid currency amount (up to two decimal places)",
                    cursor_position=len(text))  # Move the cursor to the end of the input
class FloatValidator(Validator):
# very basic validation to make sure we are inputting a float
    def validate(self, document):
        text = document.text
        if text:
            try:
                # Try converting the input to a float
                float(text)
                # You might want to add additional checks here for currency-specific validation
            except ValueError:
                # If conversion fails, raise a validation error
                raise ValidationError(message="This input is not a valid currency amount",
                                      cursor_position=len(text))
class IntValidator(Validator):
# very basic validation to make sure we are inputting a float
    def validate(self, document):
        text = document.text
        if text:
            try:
                # Try converting the input to a float
                int(text)
                # You might want to add additional checks here for currency-specific validation
            except ValueError:
                # If conversion fails, raise a validation error
                raise ValidationError(message="This input is not a valid currency amount",
                                      cursor_position=len(text))