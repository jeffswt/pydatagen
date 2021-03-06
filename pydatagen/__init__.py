
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
    # Data structures
    'deque',
    'queue',
    'stack',
    'graph',
    # Randomization methods
    'rand',
    'xrand',
    'rate',
]

import sys
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

class DequeTemplate:
    class Element:
        def __init__(self, data=None):
            self.data = data
            self.left = None
            self.right = None
        pass
    def link_element(self, l_element, r_element):
        l_element.right = r_element
        r_element.left = l_element
        return
    def __init__(self):
        self.l_elem = None
        self.r_elem = None
        self.size = 0
        return
    def push_left(self, data):
        el = self.Element(data)
        if self.size > 0:
            self.link_element(el, self.l_elem)
            self.l_elem = el
        else:
            self.l_elem = el
            self.r_elem = el
        self.size += 1
        return
    def push_right(self, data):
        el = self.Element(data)
        if self.size > 0:
            self.link_element(self.r_elem, el)
            self.r_elem = el
        else:
            self.l_elem = el
            self.r_elem = el
        self.size += 1
        return
    def get_left(self):
        if self.size <= 0:
            raise ValueError('cannot get from empty list')
        return self.l_elem.data
    def get_right(self):
        if self.size <= 0:
            raise ValueError('cannot get from empty list')
        return self.r_elem.data
    def pop_left(self):
        if self.size <= 0:
            raise ValueError('cannot pop from empty list')
        if self.l_elem.right:
            self.l_elem.right.left = None
            self.l_elem = self.l_elem.right
        else:
            self.l_elem = None
            self.r_elem = None
        self.size -= 1
        return
    def pop_right(self):
        if self.size <= 0:
            raise ValueError('cannot pop from empty list')
        if self.r_elem.left:
            self.r_elem.left.right = None
            self.r_elem = self.r_elem.left
        else:
            self.l_elem = None
            self.r_elem = None
        self.size -= 1
        return
    def is_empty(self):
        return self.size <= 0
    def get_size(self):
        return self.size
    def clear(self):
        self.l_elem = None
        self.r_elem = None
        self.empty = True
        return
    pass

class deque:
    def __init__(self):
        self.deque_base = DequeTemplate()
        return
    def __repr__(self):
        if self.deque_base.is_empty():
            return 'deque()'
        return 'deque(front: %s, back: %s, size: %d)' % (self.deque_base.get_left(), self.deque_base.get_right(), self.deque_base.get_size())
    def push_front(self, data):
        return self.deque_base.push_left(data)
    def push_back(self, data):
        return self.deque_base.push_right(data)
    def front(self):
        return self.deque_base.get_left()
    def back(self):
        return self.deque_base.get_right()
    def pop_front(self):
        return self.deque_base.pop_left()
    def pop_back(self):
        return self.deque_base.pop_right()
    def get_front(self):
        data = self.deque_base.get_left()
        self.deque_base.pop_left()
        return data
    def get_back(self):
        data = self.deque_base.get_right()
        self.deque_base.pop_right()
        return data
    def empty(self):
        return self.deque_base.is_empty()
    def size(self):
        return self.deque_base.get_size()
    def clear(self):
        return self.deque_base.clear()
    pass

class queue:
    def __init__(self):
        self.deque_base = DequeTemplate()
        return
    def __repr__(self):
        if self.deque_base.is_empty():
            return 'queue()'
        return 'queue(front: %s, size: %d)' % (self.deque_base.get_right(), self.deque_base.get_size())
    def push(self, data):
        return self.deque_base.push_left(data)
    def front(self):
        return self.deque_base.get_right()
    def pop(self):
        return self.deque_base.pop_right()
    def get(self):
        data = self.deque_base.get_right()
        self.deque_base.pop_right()
        return data
    def empty(self):
        return self.deque_base.is_empty()
    def size(self):
        return self.deque_base.get_size()
    def clear(self):
        return self.deque_base.clear()
    pass

class stack:
    def __init__(self):
        self.deque_base = DequeTemplate()
        return
    def __repr__(self):
        if self.deque_base.is_empty():
            return 'stack()'
        return 'stack(top: %s, size: %d)' % (self.deque_base.get_left(), self.deque_base.get_size())
    def push(self, data):
        return self.deque_base.push_left(data)
    def top(self):
        return self.deque_base.get_left()
    def pop(self):
        return self.deque_base.pop_left()
    def get(self):
        data = self.deque_base.get_right()
        self.deque_base.pop_right()
        return data
    def empty(self):
        return self.deque_base.is_empty()
    def size(self):
        return self.deque_base.get_size()
    def clear(self):
        return self.deque_base.clear()
    pass

class GraphTemplate:
    class Edge:
        def __init__(self, u, v, data):
            self.u = u
            self.v = v
            self.data = data
            return
        def __repr__(self):
            if not self.data:
                return '(%s -> %s)' % (repr(self.u), repr(self.v))
            return '(%s -> %s : %s)' % (repr(self.u), repr(self.v), repr(self.data))
        def __add__(self, value):
            return Edge(u, value.v, self.data + value.data)
        pass
    def __init__(self, n=0):
        self.n = n
        self.m = 0
        # Exception handling
        if type(n) != int or n < 0:
            raise ValueError('invalid number of nodes')
        # If n = 0 here, then we create the edges and relations dynamically,
        # instead of creating them statically.
        if self.n == 0:
            self.edges = {}
        else:
            self.edges = {set()} * (self.n + 1)
        # Done building (lazily)
        return
    def add_edge(self, u, v, data=None, directed=True):
        if not directed:
            self.add_edge(u, v, data, directed=True)
            self.add_edge(v, u, data, directed=True)
            return
        ed = self.Edge(u, v, data)
        if self.n == 0:
            if u not in self.edges:
                self.edges[u] = set()
        else:
            if type(u) != int or u < 0 or u > n or type(v) != int or v < 0 or v > n:
                raise ValueError('node id must be an integer')
        self.edges[u].add(ed)
        self.m += 1
        return
    def remove_edge(self, u, v, data=None, directed=True):
        if not directed:
            self.remove_edge(u, v, data, directed=True)
            self.remove_edge(v, u, data, directed=True)
            return
        if u not in self.edges:
            return
        for ed in self.edges[u]:
            if ed.v == v:
                if data == None or ed.data == data:
                    self.edges[u].remove(ed)
                    self.m -= 1
                    break
        return
    def contains(self, u, v, data):
        if u not in self.edges:
            return False
        for ed in self.edges[u]:
            if ed.v == v:
                if data == None or ed.data == data:
                    return True
        return False
    def size(self):
        return self.m
    pass

class graph:
    def __init__(self, n=0):
        self.graph_temp = GraphTemplate(n)
        self.edges = self.graph_temp.edges
        return
    def __repr__(self):
        if self.graph_temp.m == 0:
            return 'graph{}'
        pool = []
        for i in self.edges:
            for j in self.edges[i]:
                pool.append(repr(j))
        pool.sort()
        return 'graph{' + ', '.join(s for s in pool) + '}'
    def add_edge(self, u, v, data=None, directed=True):
        return self.graph_temp.add_edge(u, v, data, directed)
    def remove_edge(self, u, v, data=None, directed=True):
        return self.graph_temp.remove_edge(u, v, data, directed)
    def size(self):
        return self.graph_temp.size()
    def __contains__(self, u_v_pair):
        if len(u_v_pair) == 2:
            u, v = u_v_pair
            data = None
        elif len(u_v_pair) == 3:
            u, v, data = u_v_pair
        else:
            raise TypeError('__contains__() expected 2 or 3 arguments')
        return self.graph_temp.contains(u, v, data)
    pass

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
    # Tuple which starts indexes from 0
    elif vartype == tuple:
        # Not even a length is given!
        if len(args) <= 0:
            raise ValueError('expected tuple length, candidates: function(tuple, ...)')
        # Then we assign the rest to this itself, recursively
        length = check_type_int(args[0], 'tuple length')
        n_args = [list, length] + args[1:]
        gnratr = generator_random(*n_args)
        # Choosing items
        for i in gnratr:
            yield tuple(i[1:])
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
    rand(tuple, length, ...):
        Generates a one-dimensional tuple, with length "length", appending
          further generators after these two arguments.
        This method uses array indicing from [0], and can be unpacked.

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
