import inspect
import os


def _get_caller_function():
    return inspect.stack()[2][3]


def _format_items(items):
    return ' '.join([str(item) for item in items])


def _format_function(function_name):
    return '{name}():'.format(name=function_name)


def log(*items, **kwargs):
    name = kwargs.get('name', 'lodefile')

    line = _format_items([_format_function(_get_caller_function())] + list(items))

    with open(name, 'a') as f: 
        f.write(line)
        f.write('\n')
