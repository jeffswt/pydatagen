
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = 'pydatagen',
    version = '0.1.38',
    description = 'Random data generator library in Python',
    long_description = 'Create random data easier with pydatagen.',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Education',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Pascal',
        'Programming Language :: Python',
    ],
    keywords = 'data generator oi',
    url = 'https://github.com/jeffswt/pydatagen',
    author = 'jeffswt',
    author_email = '',
    license = 'LGPLv3',
    packages = [
        'pydatagen',
    ],
    install_requires = [
    ],
    entry_points = {
    },
)
