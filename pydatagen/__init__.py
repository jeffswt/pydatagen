
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

