import chess
import numpy as np
from chess.pgn import Game, read_game

from .utils import (
    BASE_PIECES,
    NUM_CHARS_FOR_ZEROS,
    convert_num_in_base_to_pieces,
    count_zeros_at_start,
    get_ordered_moves_and_digits,
)


class InvalidMoveException(Exception):
    pass


def move_to_str(board: chess.Board, move: chess.Move) -> str:
    """Coverts a move in a board to its index. The number of digits in the output
    depends on the total number of moves available, i.e. up to 10 moves available
    output has 1 digit; 11 to 100 moves it has 2 digits, etc.

    :param board: a chess.Board instance representing the current state of the game
    :param move: the next move to be played
    :return: a string representation of the move index
    :raises InvalidMoveException: if the move is not one of the available moves
    """

    all_moves, n_digits = get_ordered_moves_and_digits(board)

    try:
        move_ind = all_moves.index(move)
    except ValueError:
        raise InvalidMoveException(f"Invalid move: {move}")

    move_used_str = f"{move_ind:>0{n_digits}d}"

    return move_used_str


def moves_str_to_code(moves: str) -> str:
    """Converts a string containing move indexes into a string of pieces (the code)

    :param moves: string representing the move indexes
    :return: string of pieces (the code)
    """

    # A game with 22 0-index plies in a row ends in a draw by 3-move repetition
    # code: '0'*44 ('00000000000000000000000000000000000000000000')
    # game: 1. a3 a5 2. Ra2 a4 3. Ra1 Ra5 4. Ra2 Ra6 5. Ra1 Ra5 6. Ra2 Ra6
    #       7. Ra1 Ra5 8. Ra2 Ra6 9. Ra1 Ra5 10. Ra2 Ra6 11. Ra1 Ra5
    # so we can safely cap the zeros to two digits (13**2)
    num_zeros = min(count_zeros_at_start(moves), BASE_PIECES**NUM_CHARS_FOR_ZEROS)

    num_zeros_base = f"{np.base_repr(num_zeros, BASE_PIECES):>02s}"
    code_base = np.base_repr(int(moves), BASE_PIECES)

    if code_base == "0":
        code_base = ""

    temp = num_zeros_base + code_base
    code = convert_num_in_base_to_pieces(temp)

    return code


def convert_game_to_code(game: Game) -> str:
    board = game.board()

    moves_played_str = ""

    for move in game.mainline_moves():
        move_used_str = move_to_str(board, move)
        # print(move_used_str)
        moves_played_str += move_used_str
        board.push(move)

    return moves_str_to_code(moves_played_str)


def read_pgn_file(filename: str) -> Game:
    game = read_game(open(filename))

    if game is None:
        exit()

    return game


def convert_pgn_file_to_code(filename: str) -> str:
    game = read_game(open(filename))

    if game is None:
        exit()

    return convert_game_to_code(game)
