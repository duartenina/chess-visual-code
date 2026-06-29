from src.decode import convert_code_to_game
from src.draw import draw_code, draw_position, save_svg
from src.encode import convert_game_to_code, read_pgn_file

AVAILABLE_FILENAMES = [
    "wcc_2023_game_18",
    "sample_small",
    "sample_0-index_moves",
    "fools_mate",
    "algo_example",
]

if __name__ == "__main__":
    for filename in AVAILABLE_FILENAMES:
        print(f"Filename: {filename}")
        game_before = read_pgn_file(f"games/{filename}.pgn")
        print(game_before.mainline_moves())

        code = convert_game_to_code(game_before)
        print(f"Num digits: {len(code):2d} | code: {code}")

        drawing = draw_code(code)
        drawing.save_svg(f"images/{filename}.svg")

        game_after = convert_code_to_game(code)
        print(game_after.mainline_moves())

        save_svg(draw_position(game_after), f"images/{filename}_final_position.svg")
        print("")
