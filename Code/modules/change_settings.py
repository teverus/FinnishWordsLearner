from Code.constants import CONFIG
from Code.ui_functions import (
    create_a_title,
    get_user_choice,
    create_a_table,
)


class ChangeSettings:
    def __init__(self, words_per_run):
        self.words_per_run = words_per_run
        self.settings = {key: value for key, value in CONFIG.items()}
        self.run()

    def run(self):
        create_a_title("Settings")
        available_options = create_a_table(
            headers=["#", "Name".ljust(50), "Value"],
            options=list(CONFIG.keys()),
            values=list(CONFIG.values())
        )
        user_choice = get_user_choice(available_options)
        a = 1


if __name__ == "__main__":
    ChangeSettings(None)
