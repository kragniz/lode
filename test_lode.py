import os

import lode

def test_log_function():
    assert(lode.log('hello') == None)

def test_log_file_created():
    lode.log('created file')
    assert(os.path.isfile('lodefile'))
