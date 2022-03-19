from Code.constants import *
from Code.modules.change_settings import ChangeSettings
from Code.modules.start_application import StartApplication
from Code.ui_functions import create_a_title, show_options


class FinnishWordsLearner:
    def __init__(self):
        super(FinnishWordsLearner, self).__init__()

        words_per_run = int(CONFIG[Settings.WORDS_PER_RUN])

        create_a_title(WELCOME_MESSAGE)
        user_choice = show_options(
            [f"Start (practice {words_per_run} words)", "Settings", "Exit"],
            last_is_zero=True,
        )

        options = {1: StartApplication, 2: ChangeSettings, 0: exit}

        while True:
            options[user_choice](words_per_run)


if __name__ == "__main__":
    FinnishWordsLearner()
