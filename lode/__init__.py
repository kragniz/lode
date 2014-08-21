import inspect
import os


def _get_caller_function():
    return inspect.stack()[2][3]

def _format_items(items):
    return ' '.join([str(item) for item in items])


def log(*items, **kwargs):
    name = kwargs.get('name', 'lodefile')

    with open(name, 'a') as f: 
        f.write(_format_items(items))
        f.write('\n')
