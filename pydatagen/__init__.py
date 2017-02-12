
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

