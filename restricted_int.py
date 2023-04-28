from copy import deepcopy


class _RestrictedInt(int):
    def __init__(self, value=0):
        int.__init__(value)
        self._bound = None

    def __getitem__(self, bound):
        self._bound = bound
        return deepcopy(self)

    def __add__(self, other):
        assert self._bound is not None
        other = int(other)
        return _RestrictedInt(super().__add__(other) % self._bound)[self._bound]

    def __sub__(self, other):
        assert self._bound is not None
        other = int(other)
        return _RestrictedInt(super().__sub__(other) % self._bound)[self._bound]

    def __call__(self, value=0):
        return self + value


RestrictedInt = _RestrictedInt()
