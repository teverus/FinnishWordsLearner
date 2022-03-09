from Code.constants import *
from Code.functions import get_words_per_run
from Code.modules.change_settings import ChangeSettings
from Code.modules.start_application import StartApplication
from Code.ui_functions import create_a_title, show_options


class FinnishWordsLearner:
    def __init__(self):
        super(FinnishWordsLearner, self).__init__()

        words_per_run = get_words_per_run()

        create_a_title(WELCOME_MESSAGE)
        user_choice = show_options(
            [f"Start (practice {words_per_run} words)", "Settings", "Exit"],
            last_is_zero=True,
        )

        options = {1: StartApplication, 2: ChangeSettings, 0: exit}

        options[user_choice]()


if __name__ == "__main__":
    FinnishWordsLearner()
