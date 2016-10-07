
"""
pyDataGen:
Python Implementation of Data Generators

This project aims to give a full experience in generating OI data as fast as
possible, in the sense of programming complexity, not time complexity. This can
be used to mass-produce data for the sake of searching for extreme data.
"""

__all__ = [
    # Imported functions
    'randint',
    'randrange',
    'choice',
    # Outputting functions
    'printf',
    'print_oi',
    'freopen',
    'fclose',
    # Self-defined randoming functions
    'possibility',
    'reseed',
    'randlist',
    'randlist2d',
    # Self-defined classes
    'UnionFindSet',
    'Graph',
    'Tree'
]

import sys
import random

opt_stdout_handle = sys.stdout

"""
Output functions
"""

def printf(*args):
    pass

def print_oi(arg):
    pass

def freopen(path):
    pass

def fclose():
    pass

# def reseed(val):
#     pass

def possibility(rate):
    pass

def randlist(sz, rnge, **kwargs):
    pass

def randlist2d(row, column, rnge):
    pass

class UnionFindSet:
    def find(self, p):
        pass
    def union(self, p, q):
        pass
    def together(self, p, q):
        pass
    def __init__(self, n=1):
        pass
    pass

class Edge:
    def __init__(self, u, v, len=None):
        pass

class Graph:
    def get_edges(self):
        pass
    def __init__(self, n=1, m=1, **kwargs):
        pass
    pass

class Tree:
    def get_edges(self):
        pass
    def __init__(self, n=1, **kwargs):
        pass
    pass
