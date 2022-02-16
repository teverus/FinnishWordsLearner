from Code.constants import *
from Code.ui_functions import create_a_title


class FinnishWordsLearner:
    def __init__(self):
        super(FinnishWordsLearner, self).__init__()

        create_a_title(WELCOME_MESSAGE)


if __name__ == '__main__':
    FinnishWordsLearner()
