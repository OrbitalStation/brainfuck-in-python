import dispatcher
import storage
import seq_looper
import container


OPEN = "["
CLOSE = "]"
met_opening_brackets_when_ignoring_all_commands = 0


def stop_ignoring_cb(item):
    global met_opening_brackets_when_ignoring_all_commands

    if item == CLOSE:
        met_opening_brackets_when_ignoring_all_commands -= 1
    elif item == OPEN:
        met_opening_brackets_when_ignoring_all_commands += 1

    return met_opening_brackets_when_ignoring_all_commands == 0


def open_f(executor):
    global met_opening_brackets_when_ignoring_all_commands

    if storage.CurrentCell.get() != 0:
        executor(seq_looper.CommandGetCursor(container.push))
    else:
        met_opening_brackets_when_ignoring_all_commands = 1
        executor(seq_looper.CommandIgnoreTokensUntil(stop_ignoring_cb))


def close_f(executor):
    global met_opening_brackets_when_ignoring_all_commands

    if storage.CurrentCell.get() != 0:
        executor(seq_looper.CommandSetCursor(container.get_last_copied))
    else:
        container.pop()


dispatcher.register(OPEN, open_f)
dispatcher.register(CLOSE, close_f)
