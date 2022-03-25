import os
from typing import Union, List

from tabulate import tabulate

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


def show_options(options: list, title: str = None, last_is_zero: bool = False) -> int:
    available_options = []

    if title:
        print(title)

    for index, element in enumerate(options, 1):
        index = 0 if last_is_zero and index == len(options) else index
        print(f"{index} - {element}")
        available_options.append(str(index))

    user_choice = get_user_choice(available_options)

    return user_choice


def get_user_choice(available_options: List[str]) -> str:
    user_choice = input("\nPlease, enter your choice: ")

    while user_choice not in available_options:
        guidelines = ", ".join(available_options)
        print(f"[WARNING] You must enter one of these values: {guidelines}")
        user_choice = input("\nPlease, enter your choice: ")

    return user_choice


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
    remaining_correct = 50 - correct_half
    remaining_incorrect = 50 - incorrect_half
    remaining_total = 50 - total_half

    correct_bar = f"{WHITE_BLOCK_UPPER * correct_half}{DOT * remaining_correct}"
    incorrect_bar = f"{WHITE_BLOCK_UPPER * incorrect_half}{DOT * remaining_incorrect}"
    total_bar = f"{WHITE_BLOCK_FULL * total_half}{LIGHT_SHADOW * remaining_total}"

    correct = str(correct).rjust(2, "0").rjust(3)
    incorrect = str(incorrect).rjust(2, "0").rjust(3)
    total = str(total).rjust(2, "0").rjust(3)

    correct_percentage = str(correct_percentage).rjust(2, "0").rjust(3)
    incorrect_percentage = str(incorrect_percentage).rjust(2, "0").rjust(3)
    total_percentage = str(total_percentage).rjust(2, "0").rjust(3)

    print(f" PASS {correct} |{correct_bar}| {correct_percentage} %")
    print(f" FAIL {incorrect} |{incorrect_bar}| {incorrect_percentage} %")
    print(f" DONE {total} |{total_bar}| {total_percentage} %")
    create_a_border()


def get_longest_total_number(stats: dict) -> int:
    max_number = []
    for element in list(stats[Statistics.TIERS].values()):
        for key, value in element.items():
            max_number.append(value[Tier.TOTAL])

    return len(str(max(max_number))) + 1


def show_word_tiers(stats: dict):
    ____ = "".center(Tier.MAX_LENGTH)
    # max_total = get_longest_total_number(stats)
    max_total = Tier.MAX_LENGTH + 2
    current_tick = stats[Statistics.CURRENT_TIER]

    print(f" {''.center(Tier.MAX_LENGTH)} | | {'Total'.center(20)} | {'Remaining'.center(20)}")
    print("--------------------+-+----------------------+-----------------------")

    for index, (key, value) in enumerate(stats[Statistics.TIERS].items(), 1):
        name = key.center(Tier.MAX_LENGTH)

        total_low = f"{value[Tier.LOWER][Tier.TOTAL]}".center(max_total)
        total_mid = f"{value[Tier.MIDDLE][Tier.TOTAL]}".center(max_total)
        total_top = f"{value[Tier.UPPER][Tier.TOTAL]}".center(max_total)

        left_low = f"{value[Tier.LOWER][Tier.LEFT]}".center(max_total)
        left_mid = f"{value[Tier.MIDDLE][Tier.LEFT]}".center(max_total)
        left_top = f"{value[Tier.UPPER][Tier.LEFT]}".center(max_total)

        tick_low = WHITE_BLOCK_FULL if current_tick == [key, Tier.LOWER] else " "
        tick_mid = WHITE_BLOCK_FULL if current_tick == [key, Tier.MIDDLE] else " "
        tick_top = WHITE_BLOCK_FULL if current_tick == [key, Tier.UPPER] else " "

        print(f" {____} |{tick_low}| {total_low} | {left_low}")
        print(f" {name} |{tick_mid}| {total_mid} | {left_mid}")
        print(f" {____} |{tick_top}| {total_top} | {left_top}")

        if index != len(stats[Statistics.TIERS]):
            print("--------------------+-+----------------------+-----------------------")
        else:
            create_a_border("=")


def show_translate_prompt(word: str):
    print(f"\nTranslate: {word}")


def get_answer(main):
    answer = input(">>> ").strip()

    if answer == "w":
        input("Press enter to exit...")
        return False
    elif answer == "r":
        input("Press enter to restart...")
        return None
    elif answer == "q":
        exit()
    else:
        main.answer = answer.replace("a:", "ä").replace("o:", "ö")
        return True


def create_a_settings_table() -> List[str]:
    headers = ["#", "Name".ljust(50), "Value"]
    table = [
        [index, key.capitalize(), value]
        for index, (key, value) in enumerate(CONFIG.items(), 1)
    ]
    table += [[0, "Exit", ""]]

    print(tabulate(table, headers, tablefmt="orgtbl"))
    create_a_border()

    return [str(element[0]) for element in table]


def create_a_table(
    headers: list,
    options: list,
    values: list = None,
    go_back: bool = False,
    show_exit: bool = True,
    capitalize: bool = True,
    bottom_border: str = "-",
) -> List[str]:
    if values:
        table = [
            [index, key.capitalize() if capitalize else key, value]
            for index, (key, value) in enumerate(zip(options, values), 1)
        ]
    else:
        table = [
            [i, option.capitalize() if capitalize else option]
            for i, option in enumerate(options, 1)
        ]

    if show_exit:
        table += [[0, "Exit the application", ""]]

    if go_back:
        table += [["00", "Go back", ""]]

    print(tabulate(table, headers, tablefmt="presto"))
    create_a_border(bottom_border)

    return [str(element[0]) for element in table]


def create_a_table_v2(headers: list, rows: list, bottom_border: str = "-"):
    table = [[index] + row for index, row in enumerate(rows, 1)]
    print(tabulate(table, headers, tablefmt="presto"))
    create_a_border(bottom_border)
