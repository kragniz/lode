import os

import lode

def teardown_function(function):
    os.remove('lodefile')

def test_log_function_exists():
    assert(lode.log('hello') == None)

def test_log_file_created():
    lode.log('created file')
    assert(os.path.isfile('lodefile'))

def test_thing_is_logged():
    thing = 'thing with some different words'

    lode.log(thing)

    with open('lodefile') as f:
        thing_found = False
        for line in f:
            if thing in line:
                thing_found = True
    assert(thing_found)

def test_five_things_are_logged():
    things = ('one', 'two', 'three', 'four')
    things_str = ' '.join(things)

    lode.log(*things)

    with open('lodefile') as f:
        things_found = False
        for line in f:
            if things_str in line:
                things_found = True
    assert(things_found)
