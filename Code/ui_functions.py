import os

from Code.constants import SCREEN_WIDTH


def clear_screen():
    os.system("cls")


def create_a_title(text: str, upper=True):
    clear_screen()

    print(f"{'=' * SCREEN_WIDTH}")

    text = text.split("\n") if "\n" in text else text
    text = [text] if not isinstance(text, list) else text

    for line in text:
        line = line.upper() if upper else line
        print(line.center(SCREEN_WIDTH))

    print(f"{'=' * SCREEN_WIDTH}")


def create_a_border(symbol: str = "-"):
    print(f"{f'{symbol}' * SCREEN_WIDTH}")


def show_options(options: list, last_is_zero: bool = False) -> int:
    available_options = []

    for index, element in enumerate(options, 1):
        index = 0 if last_is_zero and index == len(options) else index
        print(f"{index} - {element}")
        available_options.append(str(index))

    user_choice = input("\nPlease, enter your choice: ")

    while user_choice not in available_options:
        guidelines = ", ".join(available_options)
        print(f"[WARNING] You must enter one of these values: {guidelines}")
        user_choice = input("\nPlease, enter your choice: ")

    return int(user_choice)
