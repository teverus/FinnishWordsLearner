from Code.constants import *
from Code.ui_functions import create_a_border, clear_screen


class StartApplication:
    def __init__(self):
        a = 1
        self.run()

    def run(self):
        clear_screen()
        create_a_border("=")
        print('''If you don't know a word, just hit "Enter"'''.center(SCREEN_WIDTH))
        print(''' Enter "q" or "exit" to exit | Enter "r" or "restart" to restart'''.center(SCREEN_WIDTH))
        create_a_border("=")
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
        print("")
        print("Translate: terve")
        input(">>> ")


if __name__ == '__main__':
    StartApplication()
