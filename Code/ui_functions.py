import os
from math import ceil

from Code.constants import *


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


def show_run_statistics(stats):
    correct = stats[Statistics.CORRECT]
    incorrect = stats[Statistics.INCORRECT]
    total = correct + incorrect
    words_per_run = int(CONFIG[Settings.WORDS_PER_RUN])

    correct_percentage = round(correct / total * 100)
    incorrect_percentage = round(incorrect / total * 100)
    total_percentage = round(total / words_per_run * 100)

    correct_percentage_half = round(correct_percentage / 2)
    incorrect_percentage_half = round(incorrect_percentage / 2)
    total_percentage_half = round(total_percentage / 2)
    remaining = 50 - total_percentage_half

    correct_bar = f"{WHITE_BLOCK_UPPER * correct_percentage_half}{DOT * incorrect_percentage_half}"
    incorrect_bar = f"{WHITE_BLOCK_UPPER * incorrect_percentage_half}{DOT * correct_percentage_half}"
    total_bar = f"{WHITE_BLOCK_FULL * total_percentage_half}{LIGHT_SHADOW * remaining}"

    print(f"  CORRECT  {correct:02} |{correct_bar}| {correct_percentage:02} %")
    print(f" INCORRECT {incorrect:02} |{incorrect_bar}| {incorrect_percentage:02} %")
    print(f"   TOTAL   {total:02} |{total_bar}| {total_percentage} %")
    create_a_border()
