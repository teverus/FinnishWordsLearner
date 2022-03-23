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
    create_a_table,
    show_options,
)


class StartApplication:
    def __init__(self, words_per_run):
        self.words_per_run = words_per_run
        self.snapshot = get_all_words()
        self.stats = get_stats(self.snapshot)
        self.word = Word()
        self.answer = None
        self.incorrect_answers = {}

        self.result = None
        self.run()

    def run(self):
        for _ in range(1, self.words_per_run + 1):
            get_random_word(self)

            word_title = f"[ Word {_} of {self.words_per_run} ]"
            create_a_title([word_title, USER_TIPS], upper=False)

            show_run_statistics(self.stats)
            show_word_tiers(self.stats)

            show_translate_prompt(self.word.english)
            answer = get_answer(self)

            if answer:
                score_delta = check_answer(self)

                update_word_score(self, score_delta)

                input("""Press "Enter" to continue...""")

            else:
                self.result = ExitCodes.START_THE_APPLICATION
                return

        self.show_results()

        user_choice = show_options(
            title="What would you like to do next?",
            options=["Practice more", "Exit"],
            last_is_zero=True,
        )

        if user_choice == "0":
            exit()
        else:
            self.result = ExitCodes.START_THE_APPLICATION
            return

    def show_results(self):
        create_a_title("Your results")
        show_run_statistics(self.stats)
        if self.incorrect_answers:
            create_a_table(
                headers=["#", "Correct word".center(27), "Incorrect word".center(28)],
                options=list(self.incorrect_answers.keys()),
                values=list(self.incorrect_answers.values()),
                show_exit=False,
                capitalize=False,
                bottom_border="=",
            )


if __name__ == "__main__":
    StartApplication(None)
