from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def find_packages_in_dir(path):
    return [path + x for x in find_packages(path)]


setup(
    name='opentimestamps-client',
    version='0.4.0',
    url='https://github.com/opentimestamps/opentimestamps-client',

    packages=find_packages() + find_packages_in_dir('python-opentimestamp'),

    install_requires=[
        'python-bitcoinlib>=0.7.0',
        'GitPython>=2.0.8',
        'PySocks>=1.5.0',
        'pysha3>=1.0.2',
    ],

    zip_safe=True,

    scripts={
        'ots-git-gpg-wrapper',
        'ots-git-gpg-wrapper.sh',
    },

    entry_points={
        'console_scripts': [
            'ots=otsclient.cli:main',
        ],
    },
)
