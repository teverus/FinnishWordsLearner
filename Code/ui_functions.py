import os

from Code.constants import SCREEN_WIDTH


def create_a_title(text: str):
    os.system("cls")
    print(f"{'=' * SCREEN_WIDTH}")
    print(text.upper().center(SCREEN_WIDTH))
    print(f"{'=' * SCREEN_WIDTH}")


def show_options(options: list, last_is_zero=True):
    available_options = []

    for index, element in enumerate(options, 1):
        index = 0 if last_is_zero and index == len(options) else index
        print(f"{index} - {element}")
        available_options.append(str(index))

    user_choice = input("\nPlease, enter your choice: ")

    while user_choice not in available_options:
        guidelines = ", ".join(available_options)
        print(f"\nPlease, enter one of these values: {guidelines}")
        _ = input('Hit "Enter" to try again... ')

        user_choice = input("\nPlease, enter your choice: ")

    return int(user_choice)
