from functools import wraps

import click


def apply_configs(function):

    @wraps(function)
    @click.pass_context
    def wrapper(context, *args, **kwargs):
        for key, value in context._meta.items():
            if key in kwargs and not kwargs.get(key):
                kwargs[key]= value
        return function(context, *args, **kwargs)
    return wrapper


def merge(a, b):
    type_a = type(a).__name__
    type_b = type(b).__name__

    if b is None:
        return a

    if a is None:
        return b

    if type_a != type_b:
        raise Exception("bad types")

    if type_a in ('set', 'list'):
        return a + b

    if type_a == 'dict':
        new_dict = a.copy()

        for key, value in a.items():
            new_dict[key] = merge(value, b.get(key))

        for key, value in b.items():
            if key in new_dict:
                continue

            new_dict[key] = merge(value, a.get(key))

        return new_dict

    return b
