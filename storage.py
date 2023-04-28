from cell_ty import CellType
from restricted_int import RestrictedInt


ARRAY_LEN = 30_000

_storage = [CellType() for _ in range(ARRAY_LEN)]
_cursor = RestrictedInt[ARRAY_LEN]


class CurrentCell:
    @staticmethod
    def get() -> CellType:
        return _storage[_cursor]

    @staticmethod
    def set(cell: CellType):
        _storage[_cursor] = cell


class Cursor:
    @staticmethod
    def forward():
        global _cursor
        _cursor += 1

    @staticmethod
    def backward():
        global _cursor
        _cursor -= 1
