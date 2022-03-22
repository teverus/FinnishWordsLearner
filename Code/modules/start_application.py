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
)


class StartApplication:
    def __init__(self, words_per_run):
        self.words_per_run = words_per_run
        self.snapshot = get_all_words()
        self.stats = get_stats(self.snapshot)
        self.word = Word()
        self.answer = None

        self.result = None
        self.run()

    def run(self):
        for _ in range(1, self.words_per_run + 1):
            get_random_word(self)

            word_title = f"[ Word {_:02} of {self.words_per_run} ]"
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
                self.result = Modules.START_THE_APPLICATION
                return

        self.show_results()

    def show_results(self):
        create_a_title("Your results")
        show_run_statistics(self.stats)
        a = 1


if __name__ == "__main__":
    StartApplication(None)
