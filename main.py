import code_getter
import seq_looper
import dispatcher

# noinspection PyUnresolvedReferences
import dispatch_subscribers.all


seq_looper.loop_through(iter(code_getter.get_code()), dispatcher.dispatch)
