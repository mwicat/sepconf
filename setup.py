from setuptools import setup

import os, glob

def read(fname):
    return open(fname).read()

MODULES = [os.path.splitext(fn)[0] for fn in glob.glob('*.py')]
PACKAGES = [os.path.dirname(fn) for fn in glob.glob('*/__init__.py')]


setup(
    name = "sepconf",
    version = "0.0.1",
    author = "Marek Wiewiorski",
    author_email = "mwicat@gmail.com",
    description = ("Skinny phone configuration generator"),
    license = "GPLv3",
    packages=PACKAGES,
    py_modules=MODULES,
    install_requires = ['argparse', 'argh'],
    long_description=read('README'),
    entry_points = {
        'console_scripts': [
            'sepgen = sepgen:main',
            ]
        },


)
