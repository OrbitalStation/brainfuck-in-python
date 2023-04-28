def ignore(fun, *outer_args, **outer_kwargs):
    def wrapper(*_args, **_kwargs):
        return fun(*outer_args, **outer_kwargs)
    return wrapper
