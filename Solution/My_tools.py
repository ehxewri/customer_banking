from Cust_val_input import EnterValidator
from prompt_toolkit import prompt
from rich.console import Console

def pause(pause_message):
    message = str(pause_message)
    prompt (f'{message} : ', validator=EnterValidator())
def clear():
    console = Console()
    console.clear()