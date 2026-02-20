import numpy as np
import chess
from chess.pgn import read_game, Game
from .utils import BASE13_TO_CHESS


def move_to_str(board: chess.Board, move: chess.Move) -> str:
    all_moves = sorted(board.legal_moves, key=chess.Move.uci)
    num_all_moves = len(all_moves)
    move_used = all_moves.index(move)

    n_base13_digits = int(np.ceil(np.log(num_all_moves) / np.log(13)))

    move_used_str = f"{move_used:0{n_base13_digits}d}"

    return move_used_str


def moves_str_to_code(moves: str) -> str:
    temp = np.base_repr(int(moves), 13)
    for n, char_new in enumerate(BASE13_TO_CHESS):
        char_old = np.base_repr(n, 13)
        temp = temp.replace(char_old, char_new)

    return temp


def convert_game_to_code(game: Game) -> str:
    board = game.board()

    moves_played_str = ""

    for move in game.mainline_moves():
        move_used_str = move_to_str(board, move)
        moves_played_str += move_used_str
        board.push(move)

    return moves_str_to_code(moves_played_str)


def convert_pgn_file_to_code(filename: str) -> str:
    game = read_game(open(filename))

    if game is None:
        exit()

    return convert_game_to_code(game)
