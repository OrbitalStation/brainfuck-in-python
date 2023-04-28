from input_ty import InputTy
from typing import Dict, Callable, Any


CallbackType = Callable[[Any], None]

_registered: Dict[InputTy, CallbackType] = {}


def register(code_sign: InputTy, cb):
    _registered[code_sign] = cb


def dispatch(sign, *args, **kwargs):
    try:
        _registered[sign](*args, **kwargs)
    except KeyError:
        pass
