from configparser import ConfigParser

SCREEN_WIDTH = 73
WELCOME_MESSAGE = "Welcome to Finnish Learner"
SETTINGS_FILE = "settings.ini"
SETTINGS = "settings"

WHITE_BLOCK_FULL = "\u2588"
WHITE_BLOCK_UPPER = "\u2580"
LIGHT_SHADOW = "\u2591"
DOT = "."

USER_TIPS = """If you don't know a word, just hit "Enter"\nEnter "q" or "exit" to exit | Enter "r" or "restart" to restart"""


class Settings:
    WORDS_PER_RUN = "words per run"


class Statistics:
    CORRECT = "correct"
    INCORRECT = "incorrect"
    TOTAL = "total"


config = ConfigParser()
config.read(SETTINGS_FILE)

CONFIG = config[SETTINGS]
