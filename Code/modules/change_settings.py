from Code.constants import *
from Code.ui_functions import (
    create_a_title,
    get_user_choice,
    create_a_table,
    print_a_message,
)


class ChangeSettings:
    def __init__(self, _):
        self.result = None
        self.run()

    def run(self):
        create_a_title("Settings")
        available_options = create_a_table(
            headers=["#", "Name".ljust(50), "Value"],
            options=list(CONFIG.keys()),
            values=list(CONFIG.values()),
            go_back=True,
        )
        options = {
            "1": self.change_setting,
        }

        while True:
            user_choice = get_user_choice(available_options)
            if user_choice == "0":
                exit()
            elif user_choice == "00":
                self.result = Modules.SHOW_WELCOME_SCREEN
                return
            else:
                options[user_choice](user_choice)

    @staticmethod
    def change_setting(user_choice):
        setting = list(CONFIG.keys())[int(user_choice) - 1]
        new_value = input(f'New value for "{setting.capitalize()}": ').strip()

        CONFIG_PARSER[SETTINGS][setting] = new_value
        with open(SETTINGS_FILE, "w") as config_file:
            CONFIG_PARSER.write(config_file)

        CONFIG[setting] = new_value

        print_a_message(
            f'New value for "{setting.capitalize()}" was saved', centered=True
        )


if __name__ == "__main__":
    ChangeSettings(None)
