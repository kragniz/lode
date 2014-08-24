import inspect
import os
import sys
import traceback


def _get_caller_function():
    return inspect.stack()[2][3]


def _get_caller_trace(depth=1):
    sep = ' -> '
    return sep.join([frame[3] for frame in
                    reversed(inspect.stack()[3:depth+2])]) + sep[:-1]


def _get_caller_name(depth=2):
    stack = inspect.stack()
    if len(stack) < depth + 1:
        return ''

    parentframe = stack[depth][0]

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

def _get_stack(depth=None):
    try:
        raise ZeroDivisionError
    except ZeroDivisionError:
        f = sys.exc_info()[2].tb_frame.f_back

    trace = traceback.format_list(traceback.extract_stack(f, depth))

    if depth is None:
        depth = len(trace)

    return '\n' + ''.join(trace[len(trace) - depth:-1])


def _format_items(items):
    return ' '.join([str(item) for item in items if item != ''])


def _format_function(function_name):
    return '{name}():'.format(name=function_name)


def log(*items, **kwargs):
    name = kwargs.get('name', 'lodefile')
    depth = kwargs.get('depth', 1)
    qualify = kwargs.get('qualify', False)
    traceback_depth = kwargs.get('traceback', None)

    traceback_str = ''

    if traceback_depth is not None:
        if traceback_depth == True:
            traceback_str = _get_stack()
        elif traceback_depth > 0:
            traceback_str = _get_stack(traceback_depth)

    prepend = []

    if depth > 1:
        prepend.append(_get_caller_trace(depth=depth))

    if qualify:
        prepend.append(_get_caller_name())

    prepend.append(_format_function(_get_caller_function()))

    line = _format_items(prepend + list(items))

    with open(name, 'a') as f:
        f.write(traceback_str)
        f.write(line)
        f.write('\n')
