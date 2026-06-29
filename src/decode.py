import chess
from chess.pgn import Game

from src.utils import (
    BASE_PIECES,
    NUM_CHARS_FOR_ZEROS,
    convert_pieces_to_num_in_base,
    get_ordered_moves_and_digits,
)


def code_to_moves_str(code: str) -> str:
    temp = convert_pieces_to_num_in_base(code)
    num_zeros = temp[:NUM_CHARS_FOR_ZEROS]
    temp = temp[NUM_CHARS_FOR_ZEROS:]
    moves_str = "0" * int(num_zeros, BASE_PIECES)
    if temp != "":
        moves_str += str(int(temp, BASE_PIECES))

    return moves_str


def get_next_move(board: chess.Board, moves_str: str) -> tuple[chess.Move, str]:
    all_moves, n_digits = get_ordered_moves_and_digits(board)
    move_code = moves_str[:n_digits]
    moves_str = moves_str[n_digits:]
    move_ind = int(move_code)

    move = all_moves[move_ind]

    return move, moves_str


def convert_code_to_game(code: str) -> Game:
    moves_str = code_to_moves_str(code)

    board = chess.Board()
    moves = []

    while len(moves_str) > 0:
        move, moves_str = get_next_move(board, moves_str)
        moves.append(move)
        board.push(move)

    game = Game()
    game.add_line(moves)

    return game
