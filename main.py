from tabulate import tabulate

from Code.constants import *
from Code.modules.change_settings import ChangeSettings
from Code.modules.start_application import StartApplication
from Code.ui_functions import (
    create_a_title,
    show_options,
    create_a_border,
    get_user_choice,
    create_a_table,
)


class FinnishWordsLearner:
    def __init__(self):
        super(FinnishWordsLearner, self).__init__()

        words_per_run = int(CONFIG[Settings.WORDS_PER_RUN])

        create_a_title(WELCOME_MESSAGE)

        available_options = create_a_table(
            headers=["#", "Option".ljust(60)],
            options=[f"Start (practice {words_per_run} words)", "Settings"],
        )

        user_choice = get_user_choice(available_options)

        options = {1: StartApplication, 2: ChangeSettings, 0: exit}

        while True:
            options[int(user_choice)](words_per_run)


if __name__ == "__main__":
    FinnishWordsLearner()
