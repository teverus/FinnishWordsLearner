from Code.Word import Word
from Code.constants import *
from Code.db_functions import get_all_words, update_word_score
from Code.functions import get_stats, get_random_word, check_answer
from Code.ui_functions import (
    create_a_title,
    show_run_statistics,
    show_word_tiers,
    show_translate_prompt,
    get_answer,
    show_options,
    create_a_table_old,
    show_title_head, get_user_choice,
)


class StartARun:
    def __init__(self, words_per_run):
        self.words_per_run = words_per_run
        self.snapshot = get_all_words()
        self.stats = get_stats(self.snapshot)
        self.word = Word()
        self.answer = None
        self.incorrect_answers = {}

        self.result = None
        self.index = None
        self.run()

    def run(self):
        for index in range(1, self.words_per_run + 1):
            self.index = index
            get_random_word(self)

            show_title_head(self)
            show_run_statistics(self.stats)
            show_word_tiers(self.stats)

            show_translate_prompt(self.word.english)
            answer = get_answer(self)

            if answer:
                score_delta = check_answer(self)

                update_word_score(self, score_delta)

                input("""\n Press "Enter" to continue...""")

            else:
                break

        self.show_results()

        available_options = create_a_table_old(
            headers=["What would you like to do next?"],
            rows=["Start a new run", 'Go to "Settings"', "Go to main menu"]
        )
        user_choice = get_user_choice(available_options)

        if user_choice == "0":
            exit()
        else:
            options = {
                "1": ExitCodes.START_THE_APPLICATION,
                "2": ExitCodes.GO_TO_SETTINGS,
                "3": ExitCodes.SHOW_WELCOME_SCREEN
            }
            self.result = options[user_choice]
            return

    def show_results(self):
        create_a_title("Your results")
        show_run_statistics(self.stats)
        if self.incorrect_answers:
            incorrect_answers = [
                list(self.incorrect_answers[key].values())
                for key, value in self.incorrect_answers.items()
            ]
            create_a_table_old(
                headers=["English", "Correct", "Incorrect"],
                upper_headers=True,
                rows=incorrect_answers,
                center=True,
                show_exit=False,
                capitalize_rows=False
            )


if __name__ == "__main__":
    StartARun(None)
