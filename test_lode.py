import os

import lode

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
