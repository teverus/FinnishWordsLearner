from Code.constants import SCREEN_WIDTH


def create_a_title(text):
    print(f"{'=' * SCREEN_WIDTH}")
    print(text.upper().center(SCREEN_WIDTH))
    print(f"{'=' * SCREEN_WIDTH}")
