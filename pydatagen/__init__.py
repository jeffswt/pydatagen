
"""
pyDataGen:
Python Implementation of Data Generators

This project aims to give a full experience in generating OI data and random
data in the most understood way and codes in the least bytes as possible, not
regarding the generation speed.
"""

# __all__ = [
#     # Imported functions
#     'randint',
#     'randrange',
#     'choice',
#     # Outputting functions
#     'printf',
#     'print_oi',
#     'freopen',
#     'fclose',
#     # Self-defined randoming functions
#     'possibility',
#     'reseed',
#     'randlist',
#     'randlist2d',
#     # Self-defined classes
#     'UnionFindSet',
#     'Graph',
#     'Tree'
# ]

import sys
import random

def check_vartype(val, vartype, note, varnote):
    """ check_vartype(val, vartype, note, varnote): Check if variable val can
    be converted to vartype, if could, returns the converted value, elsewise
    raises and exception incorporating the note in means of varnote."""
    if type(val) == vartype:
        return val
    type_match = True
    try:
        val = vartype(val)
    except:
        type_match = False
    if not type_match:
        if type(note) != str:
            raise ValueError('incorporated note should be a string')
        if type(varnote) != str:
            raise ValueError('incorporated variable type note should be a string')
        raise ValueError('%s should be a %s' % (note, varnote))
    return val

def check_type_float(val, note):
    """Wraps check_vartype() with floating point numbers"""
    return check_vartype(val, float, note, 'decimal number')

def check_type_int(val, note):
    """Wraps check_vartype() with integers"""
    return check_vartype(val, int, note, 'integer')

def check_type_str(val, note):
    """Wraps check_vartype() with strings"""
    return check_vartype(val, str, note, 'string')

def check_type_set(val, note):
    """Wraps check_vartype() with set"""
    return check_vartype(val, set, note, 'set')

def generator_range_int(lower_bound=1, upper_bound=1):
    """generator_range_int(lower_bound, upper_bound) -- A generator that
    infinitely chooses a number in the range [lower_bound, upper_bound]"""
    if upper_bound < lower_bound:
        raise ValueError('upper bound should not be less than the lower bound')
    while True:
        res = int(random.random() * (upper_bound - lower_bound + 1)) + lower_bound
        yield res
    return 0

def generator_range_float(lower_bound=0.0, upper_bound=1.0):
    """generator_range_float(lower_bound, upper_bound) -- A generator that
    infinitely chooses a number in the range (lower_bound, upper_bound)"""
    if upper_bound < lower_bound:
        raise ValueError('upper bound should not be less than the lower bound')
    while True:
        res = float(random.random() * (upper_bound - lower_bound) + lower_bound)
        yield res
    return 0.0

def generator_choice(objset=set()):
    """generator_choice(objset) -- A generator that infinitely chooses objects
    from the given set."""
    if type(objset) != set:
        raise ValueError('object set is not a set, literally')
    if len(objset) <= 0:
        raise ValueError('can\'t choose from an empty set')
    objset = list(objset)
    gen = generator_range_int(0, len(objset))
    while True:
        pos = next(gen)
        yield objset[pos]
    return objset[0]

def generator_list(generator, length=1):
    """generator_list(generator, length) -- A generator that creates a list of
    length and starts index from [1]."""
    if length < 1:
        raise ValueError('length should not be too short')
    while True:
        res = [None,]
        for i in range(0, length):
            val = next(generator)
            res.append(val)
        yield res
    return [None,]

def generator_list_2d(generator, rows=1, columns=1):
    """generator_list_2d(generator, rows, columns) -- A generator that creates a
    list of said rows and columns and starts index from [1][1]."""
    if rows < 1 or columns < 1:
        raise ValueError('the given table size is either too short or too thin')
    generator_1d = generator_list(generator, columns)
    while True:
        res = [ [None,] * (columns+1), ]
        for i in range(0, rows):
            val = next(generator)
            res.append(val)
        yield res
    return [None,]

