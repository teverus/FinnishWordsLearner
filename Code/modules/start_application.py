from Code.constants import *
from Code.ui_functions import create_a_border, create_a_title, show_run_statistics


class StartApplication:
    def __init__(self):
        self.stats = {
            Statistics.CORRECT: 83,
            Statistics.INCORRECT: 4,
        }
        self.run()

    def run(self):
        create_a_title(USER_TIPS, upper=False)
        show_run_statistics(self.stats)
        print(f" {''.center(18)} | | Total: 11  | Left this run: 0")
        print(f" {'Beginner'.center(18)} | | Total: 2   | Left this run: 0")
        print(f" {''.center(18)} | | Total: 3   | Left this run: 0")
        create_a_border()
        print(f" {''.center(18)} | | Total: 22  | Left this run: 0")
        print(f" {'Pre-Intermediate'.center(18)} | | Total: 44  | Left this run: 0")
        print(f" {''.center(18)} | | Total: 1   | Left this run: 0")
        create_a_border()
        print(f" {''.center(18)} | | Total: 2   | Left this run: 0")
        print(f" {'Intermediate'.center(18)} | | Total: 55  | Left this run: 0")
        print(f" {''.center(18)} |{WHITE_BLOCK_FULL}| Total: 444 | Left this run: 444")
        create_a_border()
        print(f" {''.center(18)} | | Total: 2   | Left this run: 2")
        print(f" {'Upper-Intermediate'.center(18)} | | Total: 32  | Left this run: 32")
        print(f" {''.center(18)} | | Total: 12  | Left this run: 12")
        create_a_border()
        print(f" {''.center(18)} | | Total: 32  | Left this run: 32")
        print(f" {'Advanced'.center(18)} | | Total: 45  | Left this run: 45")
        print(f" {''.center(18)} | | Total: 43  | Left this run: 43")
        create_a_border()
        print("Translate: terve")
        user_choice = input(">>> ")
        create_a_border()
        print("CORRECT :)".center(SCREEN_WIDTH))
        create_a_border()
        input("""Press "Enter" to continue...""")


if __name__ == "__main__":
    StartApplication()
