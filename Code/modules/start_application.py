from Code.constants import *
from Code.db_functions import get_all_words
from Code.functions import get_stats
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
        self.words_per_run = words_per_run
        self.all_words = get_all_words()
        self.stats = get_stats(self.all_words)
        self.run()

    def run(self):
        for attempt in range(1, self.words_per_run + 1):
            aaa = f"[ Word {attempt} of {self.words_per_run} ]"
            create_a_title([aaa, USER_TIPS], upper=False)

            show_run_statistics(self.stats)
            show_word_tiers(self.stats)

            show_translate_prompt("terve")
            answer = get_answer()

            create_a_border()
            print("CORRECT :)".center(SCREEN_WIDTH))
            create_a_border()
            input("""Press "Enter" to continue...""")


if __name__ == "__main__":
    StartApplication()
