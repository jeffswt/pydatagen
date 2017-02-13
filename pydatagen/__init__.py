
"""
pyDataGen:
Python Implementation of Data Generators

This project aims to give a full experience in generating OI data and random
data in the most understood way and codes in the least bytes as possible, not
regarding the generation speed.
"""

__all__ = [
    # Exported methods
    'printf',
    'rep',
    # Randomization methods
    'rand',
    'xrand',
    'rate',
    # Classes
    # 'DisjointSet',
    # 'Graph',
    # 'Tree',
]

import sysfd865c84930d6fd8144460e7a14e0505a8abf380
import random

################################################################################

def printf(fmt_str, *args):
    """C++ styled output function. Also automatically formats some particular
    data types for ease of output."""
    args = list(args)
    for i in range(0, len(args)):
        if type(args[i]) == list:
            args[i] = ' '.join(map(str, args[i][1:]))
    print(fmt_str % tuple(args), end='')

def rep(begin, end, step=1):
    """rep(begin, end, step=1): A wrapper for range which provides easy results
    that ends at end instead of end - 1."""
    yield from range(begin, end+1, step)

################################################################################

def check_vartype(val, vartype, note, varnote):
    """check_vartype(val, vartype, note, varnote): Check if variable val can
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
    """iterable(object): Returns if object is iterable."""
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
    if not iterable(objset):
        raise ValueError('object set is not a set, literally')
    objset = list(objset)
    if len(objset) <= 0:
        raise ValueError('can\'t choose from an empty set')
    gen = generator_range_int(0, len(objset) - 1)
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
            val = next(generator_1d)
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
    """generator_random(...): Dynamically determines which random algorithm to
    use according to the abstracted vartype given by this function. The specific
    invocation methods are listed in the rand() documentation."""
    args = list(args)
    # Defaultly integer randomization
    if len(args) <= 0:
        args.append(int)
    # Choosing from a set, blindly
    if type(args[0]) != type and (type(args[0]) != tuple or type(args[0][0]) != type):
        if not iterable(args[0]):
            raise ValueError('unable to generate set, candidates: function(iterable object)')
        objset = list(args[0])
        gnratr = generator_choice(objset)
        yield from gnratr
    vartype, *args = args
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
        yield from gnratr
    # Enforces floating point output
    elif vartype == float:
        # Default to the Python standard (0.0, 1.0), which looks all right.
        if len(args) <= 0:
            gnratr = generator_range_float(0.0, 1.0)
        # Generates with nativeness, defaults to (0.0, ...)
        elif len(args) == 1:
            upr_bnd = check_type_float(args[0], 'upper bound')
            gnratr = generator_range_float(0.0, upr_bnd)
        # Generates within open-interval range
        elif len(args) == 2:
            low_bnd = check_type_float(args[0], 'lower bound')
            upr_bnd = check_type_float(args[1], 'upper bound')
            gnratr = generator_range_float(low_bnd, upr_bnd)
        # Generates within created set, which is **probably** intended
        else:
            lst = batch_check_type(check_type_float, args, 'set item')
            gnratr = generator_choice(lst)
        # Chooses items
        yield from gnratr
    # Enforces string output
    elif vartype == str:
        """Due to the ambiguous nature of this section, variable type ambiguity
        is not allowed here. Automatic type conversion would not be enabled,
        which meant."""
        def convert_charset(input):
            output = batch_check_type(check_type_str, list(args[0]), 'character set item')
            return list(set(''.join(output)))
        # You should at least give me a length?!
        if len(args) <= 0:
            raise ValueError('expected string length, candidates: function(str, ...)')
        # Given a character set but not a length
        elif len(args) == 1 and type(args[0]) != int:
            raise ValueError('expected string length, candidates: function(str, ...)')
        # Given a length but no character set, defaults to the OI habit [a-z]
        elif len(args) == 1 and type(args[0]) == int:
            chrset = list('abcdefghijklmnopqrstuvwxyz')
            minlen = args[0]
            maxlen = args[0]
        # Given a character set and a length
        elif len(args) == 2 and iterable(args[0]) and type(args[1]) == int:
            chrset = convert_charset(args[0])
            minlen = args[1]
            maxlen = args[1]
        # Given a length range but no character set
        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            chrset = list('abcdefghijklmnopqrstuvwxyz')
            minlen = args[0]
            maxlen = args[1]
            if minlen > maxlen:
                raise ValueError('expected maximum length longer than minimum length (typo?)')
        # Given a character set and a length range
        elif len(args) == 3 and iterable(args[0]) and type(args[1]) == int and type(args[2]) == int:
            chrset = convert_charset(args[0])
            minlen = args[1]
            maxlen = args[2]
            if minlen > maxlen:
                raise ValueError('expected maximum length longer than minimum length (typo?)')
        # Otherwise not understood
        else:
            raise ValueError('ambiguous arguments, candidates: function(str, ...)')
        # Creates generators...
        chr_gnratr = generator_choice(chrset)
        if minlen == maxlen:
            gnratr = generator_string_fixed_length(chr_gnratr, minlen)
        else:
            ln_gnratr = generator_range_int(minlen, maxlen)
            gnratr = generator_string_dynamic_length(chr_gnratr, ln_gnratr)
        # Chooses items
        yield from gnratr
    # The invoker requires a list.
    elif vartype == list:
        # Not even a length is given!
        if len(args) <= 0:
            raise ValueError('expected array length, candidates: function(list, ...)')
        # Then we assign the rest to this itself, recursively
        length = check_type_int(args[0], 'array length')
        n_args = args[1:]
        i_gnratr = generator_random(*n_args)
        gnratr = generator_list(i_gnratr, length)
        # Choosing items
        yield from gnratr
    # The invoker requires a 2D matrix
    elif vartype == (list, list):
        # No length is given!
        if len(args[0]) <= 0:
            raise ValueError('expected matrix size, candidates: function((list, list), ...)')
        # Then we assign the rest to this itself, recursively
        rows, cols = args[0]
        rows = check_type_int(rows, 'matrix rows')
        cols = check_type_int(cols, 'matrix columns')
        n_args = args[1:]
        i_gnratr = generator_random(*n_args)
        gnratr = generator_list_2d(i_gnratr, rows, cols)
        # Choosing items
        yield from gnratr
    # We currently don't support the rest.
    else:
        raise ValueError('unsupported type, candidates: function(...)')
    # Ending, which ought not happen
    return

def rand(*args):
    """rand(...): An **intelligent** function which determines input type
    through the input formats dynamically. The results differs through type,
    theoretically the user is required to provide a type and consequential
    arguments.

    The documented syntaxes are as following:

    rand():
        Generates integer among [0, 65535].
    rand(iterable_object):
        Selects arbitrary items among "iterable_object".
        It is required that "iterable_object" is iterable.
    rand(int):
        Generates integer among [0, 65535].
    rand(int, upper_bound):
        Generates integer among [1, "upper_bound"].
        It is required that "upper_bound" >= 1.
    rand(int, lower_bound, upper_bound):
        Generates integer among ["lower_bound", "upper_bound"].
        It is required that "upper_bound" >= "lower_bound".
    rand(int, more_than_3_items_separated_with_commas):
        Generates integer among the items (more than 3) separated with commas.
        It is required that they are all integers.
    rand(float):
        Generates floating point number among (0.0, 1.0).
    rand(float, upper_bound):
        Generates floating point number among (0.0, "upper_bound").
        It is required that "upper_bound" >= 0.0.
    rand(float, lower_bound, upper_bound):
        Generates floating point number among ("lower_bound", "upper_bound").
        It is required that "upper_bound" >= "lower_bound".
    rand(float, more_than_3_items_separated_with_commas):
        Generates floating point number among the items (more than 3) separated
          with commas.
        It is required that they are all floating point numbers or integers.
    rand(str, length):
        Generates string of length "length" with characters [a-z].
    rand(str, min_length, max_length):
        Generates string of length in between "min_length" and "max_length",
          with characters [a-z].
        It is required that "max_length" >= "min_length".
    rand(str, character_set, length):
        Generates string of length "length" with characters in "character_set".
        It is required that it is a valid character set.
    rand(str, character_set, min_length, max_length):
        Generates string of length in between "min_length" and "max_length",
          with characters in "character_set".
        It is required that "max_length" >= "min_length".
        It is required that it is a valid character set.
    rand(list, length, ...):
        Generates a one-dimensional list / array / matrix, with length "length",
          appending further generators after these two arguments.
        It should be noted that array indicing starts from [1].
    rand((list,list), (rows,columns), ...):
        Generates a two-dimensional list / array / matrix, with "rows" rows and
          "columns" columns. Further arguments which composes the elements are
          appended after these two arguments.
        It should be noted that array indicing starts from [1][1] ([row][col]).

    The syntax should not be too hard, but easy to understand because of the
    simple nature of this function.

    Performance impact: This function brings about 3x of additional performance
    loss to general application, when using generators;
    While using direct invocations (which is strongly disrecommended), this
    brings about 75x of speed loss. So use xrand() when necessary and call
    next(generator) for faster random data generation."""
    gnratr = generator_random(*args)
    return next(gnratr)

def xrand(*args):
    """xrand(...): Generator wrapper for rand()."""
    yield from generator_random(*args)

def rate(ratio):
    """rate(ratio): Yield True at a probability of "ratio"."""
    return random.random() < ratio
