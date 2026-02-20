import numpy as np

# BASE13_TO_CHESS = "0PpNnBbRrQqKk"
BASE13_TO_CHESS = "0kKqQrRbBnNpP"


def index_to_coord(ind: int) -> tuple[int, int]:
    sql = int(np.ceil(np.sqrt(ind + 1)))
    x = min(ind + 1 - (sql - 1) ** 2, sql)
    y = min(sql, sql**2 - ind)

    return x, y
