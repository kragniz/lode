====
lode
====

.. image:: https://pypip.in/v/lode/badge.png
    :target: https://pypi.python.org/pypi/lode
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/kragniz/lode.png?branch=master
    :target: https://travis-ci.org/kragniz/lode

Tiny and minimalistic logging utility module.

Lode is designed to be used in the case where normally simple print statement
style debugging would be useful, like checking whether or not a section of code
is executed, but stdout or stderr has been robbed from you by something like a
devilishly clever test framework.  Rather than try to uncover which dark
alleyway your calls to print end up, lode just outputs it to a friendly file.

Lode is tested and supported on python versions 2.6, 2.7, 3.2, 3.3 and 3.4.


Installing
==========

Lode can be installed with pip:

.. code:: bash

    $ pip install lode


Or from source:

.. code:: bash

    $ git clone https://github.com/kragniz/lode.git
    $ cd lode
    $ python setup.py install


Using this thing
================

For the most basic usage, just import lode and call the `log` function. Usage
is largely the same as the print function, with it taking any number of
positional arguments, formatting those to a string, and joining them together
separated by spaces.

.. code:: python

    import lode; lode.log('hi there!')


Tests
=====

Tests are stored the `tests` subdirectory of the main lode package. Set up lode
for testing by running in the root directory of the git repository the
following commands:

.. code:: bash

    $ pip install -e .
    $ pip install -r test-requirements.txt

Then run the tests:

.. code:: bash

    $ py.test -v
