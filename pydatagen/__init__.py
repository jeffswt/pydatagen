
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

def batch_check_type(func, lst, note):
    """Wraps func for checking each item in list"""
    if type(lst) != list:
        raise ValueError('should provide a list for this check')
    res = []
    for i in lst:
        res.append(func(i, note))
    return res

def iterable(object):
    """Returns if object is iterable."""
    return hasattr(object, '__iter__')

################################################################################

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

def generator_choice(objset=list()):
    """generator_choice(objset) -- A generator that infinitely chooses objects
    from the given set."""
    if not iterable(objset)
        raise ValueError('object set is not a set, literally')
    objset = list(objset)
    if len(objset) <= 0:
        raise ValueError('can\'t choose from an empty set')
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

def generator_list_dynamic_length(generator, length_generator):
    """generator_list(generator, length_generator) -- A generator that creates a
    list of dynamic length and starts index from [1]."""
    while True:
        res = [None,]
        length = next(length_generator)
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

def generator_string_fixed_length(generator, length=1):
    """generator_string_fixed_length(generator, length) -- Wraps generator_list()
    but yields strings as results. Length is constant."""
    generator_l = generator_list(generator, length)
    while True:
        res = ''.join(next(generator_l)[1:])
        yield res
    return ''

def generator_string_dynamic_length(generator, length_generator):
    """generator_string_dynamic_length(generator, length_generator) -- Wraps
    generator_list() but yields strings as results. Length is dynamic, and the
    user is responsible for checking the consistency of generated length."""
    generator_l = generator_list_dynamic_length(generator, length_generator)
    while True:
        res = ''.join(next(generator_l)[1:])
        yield res
    return ''

def generator_random(*args):
    """Dynamically determines which random algorithm to use according to the
    abstracted vartype given by this function. The specific invocation methods
    are listed in the rand() documentation."""
    # Defaultly integer randomization
    if len(args) <= 0:
        args.append(int)
    vartype = args[0]
    args = args[:-1]
    # Choosing from a set, blindly
    if type(args[0]) != type and (type(args[0]) != tuple or type(args[0][0]) != type):
        if not iterable(args[0]):
            raise ValueError('unable to generate set, candidates: function(iterable object)')
        objset = list(args[0])
        gnratr = generator_choice(objset)
        while True:
            yield next(gnratr)
        pass
    # Enforces integer output
    if vartype == int:
        # Default to the C++ standard, [0, 65535]
        if len(args) <= 0:
            gnratr = generator_range_int(0, 65535)
        # Default to the OI de-facto standard, [1, ...]
        elif len(args) == 1:
            upr_bnd = check_type_int(args[0], 'upper bound')
            gnratr = generator_range_int(1, upr_bnd)
        # Generates within closed-interval range
        elif len(args) == 2:
            low_bnd = check_type_int(args[0], 'lower bound')
            upr_bnd = check_type_int(args[1], 'upper bound')
            gnratr = generator_range_int(low_bnd, upr_bnd)
        # Generates within created set, which is **probably** intended
        else:
            lst = batch_check_type(check_type_int, args, 'set item')
            gnratr = generator_choice(lst)
        # Chooses items
        while True:
            yield next(gnratr)
        pass
    # Enforces floating point output
    elif vartype == float:
        # Default to the Python standard (0.0, 1.0), which looks all right.
        if len(args) <= 0:
            gnratr = generator_range_float(0.0, 1.0)
        # Generates with nativeness, defaults to (0.0, ...)
        elif len(args) == 1:
            upr_bnd = check_type_float(args[0], 'upper bound')
            gnratr = generator_range_int(0.0, upr_bnd)
        # Generates within open-interval range
        elif len(args) == 2:
            low_bnd = check_type_float(args[0], 'lower bound')
            upr_bnd = check_type_float(args[1], 'upper bound')
            gnratr = generator_range_int(low_bnd, upr_bnd)
        # Generates within created set, which is **probably** intended
        else:
            lst = batch_check_type(check_type_float, args, 'set item')
            gnratr = generator_choice(lst)
        # Chooses items
        while True:
            yield next(gnratr)
        pass
