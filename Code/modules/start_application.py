from Code.Word import Word
from Code.constants import *
from Code.db_functions import get_all_words
from Code.functions import get_stats, get_random_word
from Code.ui_functions import (
    create_a_border,
    create_a_title,
    show_run_statistics,
    show_word_tiers,
    show_translate_prompt,
    get_answer,
)


class StartApplication:
    def __init__(self, words_per_run):
        self.words_in_run = words_per_run
        self.all_words = get_all_words()
        self.snapshot = self.all_words.copy()
        self.stats = get_stats(self.all_words)
        self.word = Word()

        self.run()

    def run(self):
        for _ in range(1, self.words_in_run + 1):
            get_random_word(self)

            create_a_title([TITLE.format(_, self.words_in_run), USER_TIPS], upper=False)

            show_run_statistics(self.stats)
            show_word_tiers(self.stats)

            show_translate_prompt(self.word.finnish)
            answer = get_answer()

            create_a_border()
            print("CORRECT :)".center(SCREEN_WIDTH))
            create_a_border()
            input("""Press "Enter" to continue...""")


if __name__ == "__main__":
    StartApplication(None)
