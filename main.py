from IPython.display import display
from src.create import convert_pgn_file_to_code
from src.draw import draw_code


FILENAME = "games/wcc_2023_game_18.pgn"
# FILENAME = "games/sample_tiny.pgn"


if __name__ == "__main__":
    display(draw_code(convert_pgn_file_to_code(FILENAME)))
