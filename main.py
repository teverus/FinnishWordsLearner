from Code.constants import CONFIG, Settings, WELCOME_MESSAGE
from Code.modules.change_settings import ChangeSettings
from Code.modules.start_application import StartApplication
from Code.ui_functions import (
    create_a_title,
    get_user_choice,
    create_a_table,
)


class FinnishWordsLearner:
    def __init__(self):
        super(FinnishWordsLearner, self).__init__()

        self.words_per_run = int(CONFIG[Settings.WORDS_PER_RUN])

        self.options = {
            "1": StartApplication,
            "2": ChangeSettings,
            "0": exit,
            "00": self.show_welcome_screen,
        }

        choice = self.show_welcome_screen()

        while True:
            self.words_per_run = int(CONFIG[Settings.WORDS_PER_RUN])
            choice = self.options[choice]() if choice in ["0", "00"] else choice

            module = self.options[choice](self.words_per_run)
            choice = module.result

    def show_welcome_screen(self):
        create_a_title(WELCOME_MESSAGE)

        available_options = create_a_table(
            headers=["Option"],
            rows=[f"Start (words to practice: {self.words_per_run})", "Settings"],
        )

        user_choice = get_user_choice(available_options)

        return user_choice


if __name__ == "__main__":
    FinnishWordsLearner()
