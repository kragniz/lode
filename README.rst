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
alleyway your calls to print end up, lode just outputs it to a friendly file. A
beacon of hope in dark land

Installing
==========

.. code:: bash

    $ pip install lode

Using this thing
================

.. code:: python

    import lode; lode.log('hi there!')
