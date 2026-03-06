import drawsvg as dw
import numpy as np
from .utils import index_to_coord

SQUARE_COLORS = ["#a67b5a", "#6b3912"]


def coord_to_center_pos(
    coord: tuple[int, int], square_size: float
) -> tuple[float, float]:
    x, y = coord
    cx = (x - 0.5) * square_size
    cy = (y - 0.5) * square_size

    return cx, cy


def draw_base_board(svg: dw.Drawing, n: int, square_size: float = 30) -> dw.Drawing:
    for row in range(n):
        for col in range(n):
            x = row * square_size
            y = col * square_size
            color = SQUARE_COLORS[(row + col) % 2]

            square = dw.Rectangle(
                x=x, y=y, width=square_size, height=square_size, fill=color
            )
            svg.append(square)

    return svg


def get_svg_for_piece(
    piece_in_fen: str, center: tuple[float, float] = (0, 0), piece_size: float = 25
) -> dw.Image:
    cx, cy = center
    cx, cy = cx - piece_size / 2, cy - piece_size / 2

    piece_u = piece_in_fen.upper()
    piece_color = "l" if piece_in_fen == piece_u else "d"
    filename = f"pieces/{piece_color}{piece_u}.svg"

    return dw.Image(
        x=cx, y=cy, width=piece_size, height=piece_size, path=filename, embed=True
    )


def draw_pieces(svg: dw.Drawing, code: str, square_size: float = 30) -> dw.Drawing:
    piece_size = square_size * 0.9

    for ind, piece in enumerate(code):
        if piece == "0":
            continue

        coord = index_to_coord(ind)
        center = coord_to_center_pos(coord, square_size)
        piece_svg = get_svg_for_piece(piece, center, piece_size)
        svg.append(piece_svg)

    return svg


def draw_svg(size: float) -> dw.Drawing:
    canvas = dw.Drawing(size, size)

    return canvas


def draw_code(code: str, square_size: float = 30) -> dw.Drawing:
    n = int(np.ceil(np.sqrt(len(code))))
    print(n)
    size = square_size * n

    svg = draw_svg(size)
    svg = draw_base_board(svg, n, square_size)
    svg = draw_pieces(svg, code, square_size)

    return svg
