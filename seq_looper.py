from copy import deepcopy
from typing import Callable, Iterator
from input_ty import InputTy


class Command:
    pass


class CommandGetCursor(Command):
    def __init__(self, cb: Callable[[Iterator[InputTy]], None]):
        self.cb = cb


class CommandSetCursor(Command):
    def __init__(self, cb: Callable[[], Iterator[InputTy]]):
        self.cb = cb


class CommandIgnoreCellsUntil(Command):
    def __init__(self, cb: Callable[[InputTy], bool]):
        self.cb = cb


Executor = Callable[[Command], None]


def loop_through(seq: Iterator[InputTy], callback: Callable[[InputTy, Executor], None]):
    do_ignore = False
    ignore_stop_cb = None

    def executor(command: Command):
        nonlocal seq, do_ignore, ignore_stop_cb
        if isinstance(command, CommandGetCursor):
            command.cb(deepcopy(seq))
        elif isinstance(command, CommandSetCursor):
            seq = command.cb()
        elif isinstance(command, CommandIgnoreCellsUntil):
            do_ignore = True
            ignore_stop_cb = command.cb
        else:
            raise ValueError("unknown command")

    while (item := next(seq, None)) is not None:
        if do_ignore:
            # noinspection PyCallingNonCallable
            if ignore_stop_cb(item):
                do_ignore = False
        else:
            callback(item, executor)
