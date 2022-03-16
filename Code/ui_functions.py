import os
from typing import Union

from Code.constants import *


def do_nothing():
    pass


def clear_console():
    os.system("cls")


def print_a_message(
    message: Union[str, list],
    centered: bool = False,
    upper: bool = False,
    clear_screen: bool = False,
    border: str = "-",
):
    clear_console() if clear_screen else do_nothing()

    print(f"{border * SCREEN_WIDTH}") if border else do_nothing()

    message = [message] if not isinstance(message, list) else message

    for index, element in enumerate(message):
        if "\n" in element:
            del message[index]
            new_index = index
            new_elements = element.split("\n")
            for new_element in new_elements:
                message.insert(new_index, new_element)
                new_index += 1

    for line in message:
        line = line.upper() if upper else line
        line = line.center(SCREEN_WIDTH) if centered else line
        print(line)

    print(f"{border * SCREEN_WIDTH}") if border else do_nothing()


def create_a_title(text: Union[str, list], upper=True):
    print_a_message(text, centered=True, upper=upper, clear_screen=True, border="=")


def create_a_border(symbol: str = "-"):
    print(f"{symbol * SCREEN_WIDTH}")


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


def show_run_statistics(stats: dict):
    correct = stats[Statistics.CORRECT]
    incorrect = stats[Statistics.INCORRECT]
    total = correct + incorrect
    words_per_run = int(CONFIG[Settings.WORDS_PER_RUN])

    try:
        correct_percentage = round(correct / total * 100)
    except ZeroDivisionError:
        correct_percentage = 0
    try:
        incorrect_percentage = round(incorrect / total * 100)
    except ZeroDivisionError:
        incorrect_percentage = 0
    total_percentage = round(total / words_per_run * 100)

    correct_half = round(correct_percentage / 2)
    incorrect_half = round(incorrect_percentage / 2)
    total_half = round(total_percentage / 2)
    remaining_correct = 50 - incorrect_half
    remaining_incorrect = 50 - correct_half
    remaining_total = 50 - total_half

    correct_bar = f"{WHITE_BLOCK_UPPER * correct_half}{DOT * remaining_correct}"
    incorrect_bar = f"{WHITE_BLOCK_UPPER * incorrect_half}{DOT * remaining_incorrect}"
    total_bar = f"{WHITE_BLOCK_FULL * total_half}{LIGHT_SHADOW * remaining_total}"

    print(f"  CORRECT  {correct:02} |{correct_bar}| {correct_percentage:02} %")
    print(f" INCORRECT {incorrect:02} |{incorrect_bar}| {incorrect_percentage:02} %")
    print(f"  OVERALL  {total:02} |{total_bar}| {total_percentage:02} %")
    create_a_border()


def get_longest_total_number(stats: dict) -> int:
    max_number = []
    for element in list(stats[Statistics.TIERS].values()):
        for key, value in element.items():
            max_number.append(value[Tier.TOTAL])

    return len(str(max(max_number))) + 1


def show_word_tiers(stats: dict):
    ____ = "".center(Tier.MAX_LENGTH)
    max_total = get_longest_total_number(stats)
    current_tick = stats[Statistics.CURRENT_TIER]

    for key, value in stats[Statistics.TIERS].items():
        name = key.center(Tier.MAX_LENGTH)

        total_low = f"{value[Tier.LOWER][Tier.TOTAL]}".ljust(max_total)
        total_mid = f"{value[Tier.MIDDLE][Tier.TOTAL]}".ljust(max_total)
        total_top = f"{value[Tier.UPPER][Tier.TOTAL]}".ljust(max_total)

        left_low = f"{value[Tier.LOWER][Tier.LEFT]}".ljust(max_total)
        left_mid = f"{value[Tier.MIDDLE][Tier.LEFT]}".ljust(max_total)
        left_top = f"{value[Tier.UPPER][Tier.LEFT]}".ljust(max_total)

        tick_low = WHITE_BLOCK_FULL if current_tick == [key, Tier.LOWER] else " "
        tick_mid = WHITE_BLOCK_FULL if current_tick == [key, Tier.MIDDLE] else " "
        tick_top = WHITE_BLOCK_FULL if current_tick == [key, Tier.UPPER] else " "

        print(f" {____} |{tick_low}| Total: {total_low}| Left this run: {left_low}")
        print(f" {name} |{tick_mid}| Total: {total_mid}| Left this run: {left_mid}")
        print(f" {____} |{tick_top}| Total: {total_top}| Left this run: {left_top}")

        create_a_border()


def show_translate_prompt(word: str):
    print(f"Translate: {word}")


def get_answer(main):
    answer = input(">>> ").strip()

    if answer in ["q", "exit"]:
        input("Press enter to exit...")
        exit()
    elif answer in ["r", "restart"]:
        input("Press enter to restart...")
        return None
    else:
        main.answer = answer.replace("a:", "ä").replace("o:", "ö")
