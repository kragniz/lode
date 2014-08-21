import inspect
import os


def _get_caller_function():
    return inspect.stack()[2][3]


def _get_caller_trace(depth=1):
    sep = ' -> '
    return sep.join([frame[3] for frame in
        reversed(inspect.stack()[3:depth+2])]) + sep[:-1]


def _format_items(items):
    return ' '.join([str(item) for item in items])


def _format_function(function_name):
    return '{name}():'.format(name=function_name)


def log(*items, **kwargs):
    name = kwargs.get('name', 'lodefile')
    depth = kwargs.get('depth', 1)

    line = _format_items([_get_caller_trace(depth=depth), _format_function(_get_caller_function())] + list(items))

    with open(name, 'a') as f: 
        f.write(line)
        f.write('\n')
