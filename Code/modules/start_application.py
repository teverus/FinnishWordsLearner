from Code.constants import *
from Code.functions import get_answer
from Code.ui_functions import (
    create_a_border,
    create_a_title,
    show_run_statistics,
    show_word_tiers, show_translate_prompt,
)


class StartApplication:
    def __init__(self):
        self.stats = {
            Statistics.CORRECT: 83,
            Statistics.INCORRECT: 4,
            Statistics.TIERS: {
                Tier.BEGINNER: {
                    Tier.LOWER: {Tier.TOTAL: 1, Tier.LEFT: 2},
                    Tier.MIDDLE: {Tier.TOTAL: 3, Tier.LEFT: 4},
                    Tier.UPPER: {Tier.TOTAL: 5, Tier.LEFT: 6},
                },
                Tier.PRE_INTERMEDIATE: {
                    Tier.LOWER: {Tier.TOTAL: 7, Tier.LEFT: 8},
                    Tier.MIDDLE: {Tier.TOTAL: 9, Tier.LEFT: 10},
                    Tier.UPPER: {Tier.TOTAL: 11, Tier.LEFT: 12},
                },
                Tier.INTERMEDIATE: {
                    Tier.LOWER: {Tier.TOTAL: 13, Tier.LEFT: 14},
                    Tier.MIDDLE: {Tier.TOTAL: 15, Tier.LEFT: 16},
                    Tier.UPPER: {Tier.TOTAL: 17, Tier.LEFT: 18},
                },
                Tier.UPPER_INTERMEDIATE: {
                    Tier.LOWER: {Tier.TOTAL: 19, Tier.LEFT: 20},
                    Tier.MIDDLE: {Tier.TOTAL: 21, Tier.LEFT: 22},
                    Tier.UPPER: {Tier.TOTAL: 23, Tier.LEFT: 24},
                },
                Tier.ADVANCED: {
                    Tier.LOWER: {Tier.TOTAL: 25, Tier.LEFT: 26},
                    Tier.MIDDLE: {Tier.TOTAL: 27, Tier.LEFT: 28},
                    Tier.UPPER: {Tier.TOTAL: 29, Tier.LEFT: 30},
                },
            },
            Statistics.CURRENT_TIER: [Tier.BEGINNER, Tier.LOWER],
        }
        self.run()

    def run(self):
        create_a_title(USER_TIPS, upper=False)
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
