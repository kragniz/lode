try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name='lode',
    version='0.3.0',
    author='Louis Taylor',
    author_email='kragniz@gmail.com',
    description=('Tiny and minimalistic logging utility'),
    long_description=long_description,
    license='GPL',
    keywords='logging debugging',
    url='https://github.com/kragniz/lode',
    packages=['lode'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
