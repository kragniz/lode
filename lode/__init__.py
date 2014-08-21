import gc
import inspect
import os


def _get_caller_function():
    return inspect.stack()[2][3]


def _get_caller_trace(depth=1):
    sep = ' -> '
    return sep.join([frame[3] for frame in
        reversed(inspect.stack()[3:depth+2])]) + sep[:-1]


def _get_caller_name(depth=2):
    stack = inspect.stack()
    start = 0 + depth
    if len(stack) < start + 1:
      return ''

    parentframe = stack[start][0]

    name = []
    module = inspect.getmodule(parentframe)
    if module:
        name.append(module.__name__)

    if 'self' in parentframe.f_locals:
        name.append(parentframe.f_locals['self'].__class__.__name__)

    codename = parentframe.f_code.co_name

    if codename != '<module>':
        name.append(codename)
    del parentframe

    return ".".join(name)


def _format_items(items):
    return ' '.join([str(item) for item in items])


def _format_function(function_name):
    return '{name}():'.format(name=function_name)


def log(*items, **kwargs):
    name = kwargs.get('name', 'lodefile')
    depth = kwargs.get('depth', 1)
    qualify = kwargs.get('qualify', False)

    prepend = []

    if depth > 1:
        prepend.append(_get_caller_trace(depth=depth))

    if qualify:
        prepend.append(_get_caller_name())

    prepend.append(_format_function(_get_caller_function()))

    line = _format_items(prepend + list(items))

    with open(name, 'a') as f: 
        f.write(line)
        f.write('\n')
