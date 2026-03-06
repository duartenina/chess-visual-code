from math import ceil, log

import chess
import numpy as np

BISHOP_LETTER = "x"
# bishops can be mistaken with base-13 'b' (11),
# so they're marked as BISHOP_LETTER
BASE_TO_CHESS = f"0kKqQrR{BISHOP_LETTER}{BISHOP_LETTER.upper()}nNpP"
BASE_PIECES = len(BASE_TO_CHESS)  # 13
NUM_CHARS_FOR_ZEROS = 2


def bishops_to_temp(pieces: str) -> str:
    pieces = pieces.replace("b", BISHOP_LETTER.lower())
    pieces = pieces.replace("B", BISHOP_LETTER.upper())

    return pieces


def temp_to_bishops(pieces: str) -> str:
    pieces = pieces.replace(BISHOP_LETTER.lower(), "b")
    pieces = pieces.replace(BISHOP_LETTER.upper(), "B")

    return pieces


def convert_num_in_base_to_pieces(num: str) -> str:
    pieces = num
    for n, piece_char in enumerate(BASE_TO_CHESS):
        base_repr = np.base_repr(n, BASE_PIECES)
        pieces = pieces.replace(base_repr, piece_char)

    return temp_to_bishops(pieces)


def convert_pieces_to_num_in_base(pieces: str) -> str:
    num = bishops_to_temp(pieces)
    for piece_char in BASE_TO_CHESS:
        base_repr = np.base_repr(BASE_TO_CHESS.index(piece_char), BASE_PIECES)
        num = num.replace(piece_char, base_repr)

    return num


def index_to_coord(ind: int) -> tuple[int, int]:
    sql = int(np.ceil(np.sqrt(ind + 1)))
    x = min(ind + 1 - (sql - 1) ** 2, sql)
    y = min(sql, sql**2 - ind)

    return x, y


def get_ordered_moves_and_digits(
    board: chess.Board, base: int = 10
) -> tuple[list[chess.Move], int]:
    all_moves = sorted(board.legal_moves, key=chess.Move.uci)
    num_all_moves = len(all_moves)
    n_digits = max(int(ceil(log(num_all_moves - 1) / log(base))), 1)

    return all_moves, n_digits


def count_zeros_at_start(num: str) -> int:
    if len(num) == 0:
        return 0

    count = 0
    for char in num:
        if char == "0":
            count += 1
        else:
            break

    return count
