from Code.constants import *
from Code.ui_functions import create_a_border, create_a_title


class StartApplication:
    def __init__(self):
        a = 1
        self.run()

    def run(self):
        create_a_title(USER_TIPS, upper=False)
        aaa = "\u2580"
        zzz = "."
        print(f"  CORRECT  20 |{aaa * 20}{zzz * 30}| 40 %")
        print(f" INCORRECT 30 |{aaa * 30}{zzz * 20}| 60 %")
        print(f"   TOTAL   50 |{WHITE_BLOCK_FULL * 25}{LIGHT_SHADOW * 25}| 50 %")
        create_a_border()
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
