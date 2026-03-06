from IPython.display import display
from src.encode import convert_pgn_file_to_code
from src.draw import draw_code


FILENAME = "wcc_2023_game_18"
# FILENAME = "games/sample_tiny.pgn"


if __name__ == "__main__":
    drawing = draw_code(convert_pgn_file_to_code(f"games/{FILENAME}.pgn"))
    drawing.save_svg(f"images/{FILENAME}.svg")
