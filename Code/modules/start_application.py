from Code.ui_functions import create_a_title, create_a_border


class StartApplication:
    def __init__(self):
        a = 1
        self.run()

    def run(self):
        create_a_title("123")
        print(f" {''.center(18)} | | Total: 11  | Left: ")
        print(f" {'Beginner'.center(18)} | | Total: 2   | Left: ")
        print(f" {''.center(18)} | | Total: 3   | Left: ")
        create_a_border()
        print(f" {''.center(18)} | | Total: 22  | Left: ")
        print(f" {'Pre-Intermediate'.center(18)} | | Total: 44  | Left: ")
        print(f" {''.center(18)} | | Total: 1   | Left: ")
        create_a_border()
        print(f" {''.center(18)} | | Total: 2   | Left: ")
        print(f" {'Intermediate'.center(18)} | | Total: 55  | Left: ")
        print(f" {''.center(18)} |\u2588| Total: 444 | Left: ")
        create_a_border()
        print(f" {''.center(18)} | | Total: 2   | Left: ")
        print(f" {'Upper-Intermediate'.center(18)} | | Total: 32  | Left: ")
        print(f" {''.center(18)} | | Total: 12  | Left: ")
        create_a_border()
        print(f" {''.center(18)} | | Total: 32  | Left: ")
        print(f" {'Advanced'.center(18)} | | Total: 45  | Left: ")
        print(f" {''.center(18)} | | Total: 43  | Left: ")
        create_a_border()
        print("")
        print("Translate: Terve")
        input(">>> ")


if __name__ == '__main__':
    StartApplication()
