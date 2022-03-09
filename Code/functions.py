from configparser import ConfigParser

from Code.constants import *


def get_words_per_run() -> str:
    config = ConfigParser()
    config.read(SETTINGS_FILE)

    return config[SETTINGS][Settings.WORDS_PER_RUN]