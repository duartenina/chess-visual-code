from IPython.display import display
import chess
from chess.svg import board as board2svg
from src.create import convert_pgn_file_to_fen


# FILENAME = "games/wcc_2023_game_18.pgn"
FILENAME = "games/short_sample.pgn"


def show_board(board: chess.Board):
    display(board2svg(board, size=300, coordinates=False))


if __name__ == "__main__":
    show_board(chess.Board(convert_pgn_file_to_fen(FILENAME)))
