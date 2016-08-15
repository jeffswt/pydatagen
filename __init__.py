
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
from random import *

opt_stdout_handle = sys.stdout
opt_random_seed = 4567

"""
Output functions
"""

"""
This function gives the given input to the desired output file handle, which
can be overloaded by specifying output file name through freopen(). The function
prints whatever given, and does not intrigue following line breaks.
"""
def printf(*args):
    fout = opt_stdout_handle
    for arg in args:
        fout.write(str(arg))
    fout.flush()

def print_oi(arg):
    """OI Styled printing in Python, specially optimized for arrays
    and 2-D arrays, in a globally acceptable OI data input style.
    Do not use this if you are willing to customize the style.
    Exempli gratis:
        >>> from pydatagen import *
        >>> my_list = [[1, 5, 3, 7], [2, 6, 5, 9], [3, 7, 15, 33]]
        >>> print_oi(my_list)
        1 5 3 7
        2 6 5 9
        3 7 15 33
        >>> my_list = [45, 2, 7, 39]
        >>> print_oi(my_list)
        45 2 7 39
    """
    if type(arg) == list:
        all_list = True
        for it in arg:
            if type(it) != list:
                all_list = False
                break
        if all_list:
            for i in arg:
                for j in i:
                    printf('%s ' % j)
                printf('\n')
        else:
            for i in arg:
                printf('%s ' % i)
            printf('\n')
    elif type(arg) == Graph:
        printf('%d %d\n' % (arg.n, arg.m))
        for ed in arg.get_edges():
            printf('%d %d ' % (ed.u, ed.v))
            if ed.len: printf('%s ' % ed.len)
            printf('\n')
    elif type(arg) == Tree:
        printf('%d\n' % (arg.n))
        for ed in arg.get_edges():
            printf('%d %d ' % (ed.u, ed.v))
            if ed.len: printf('%s ' % ed.len)
            printf('\n')
    else:
        printf(arg)
    return

def freopen(path):
    """Reload standard output handle for pydatagen.printf(). This
    can be used to override data output, but reloading to standard
    output has not yet implemented. This would require fclose()ing
    the handle, and it would be reset to stdout.
    """
    if type(opt_stdout_handle) == file:
        opt_stdout_handle.close()
    opt_stdout_handle = open(path, 'w')
    return opt_stdout_handle

def fclose():
    """Finally close the output handle and leave it alone. The file
    handle / stdout will be finally accessible from other
    applications. Exempli gratis:
        >>> from pydatagen import *
        >>> freopen('test.txt')
        >>> printf('Hello, world!')
        >>> fclose()
    """
    opt_stdout_handle.close()
    opt_stdout_handle = sys.stdout
    return

def reseed(val):
    """This would invoke the random engine to use another defined
    random seed, making automatic OJs available. This would merely
    require the data generator indexer to only store a seed
    instead of a vast amount of data. Exempli gratis:
        >>> from pydatagen import *
        >>> randrange(1, 1000)
        618
        >>> randrange(1, 1000)
        391
        >>> reseed(666)
        >>> randrange(1, 1000)
        468
        >>> reseed(666)
        >>> randrange(1, 1000)
        468
    """
    opt_random_seed = val
    seed(val)
    return

def possibility(rate):
    """This function always returns a boolean value, which indicates to be
    successful or not. The rate should be a real number that ranges between
    0 and 1, specifying the possibility of this action. The procedure would
    randomly choose a possibility between this range and amortizedly, in a
    specified range of rate.
        >>> from pydatagen import *
        >>> possibility(0.5)
        True
        >>> possibility(0.5)
        False
    """
    if rate < 0 or rate > 1:
        return False
    # A valid input
    if rate == 0:
        return False
    if rate == 1:
        return True
    # Previously were definite invocations.
    p = choice(range(0, 1000000)) % 1000 + 1
    q = int(rate * 1000)
    if p <= q:
        return True
    return False

def randlist(sz, rnge, **kwargs):
    """This function generates a list of 'sz' items from the given
    range or list / array. The 'rnge' parameter can be specified
    by anything ranging from 'range' to 'list', any which could be
    fit into 'choice' may be available. Exempli gratis:
        >>> from pydatagen import *
        >>> randlist(6, range(100, 999))
        [737, 683, 108, 853, 177, 233]
        >>> randlist(3, ['INSERT', 'DELETE', 'SUM', 'MIN', 'REVERSE', 'REVOLVE'])
        ['REVOLVE', 'SUM', 'REVERSE']
    """
    res = list()
    distinct = 'distinct' in kwargs and kwargs['distinct']
    if distinct:
        if len(rnge) > 1.2 * sz:
            dres = dict()
            for i in range(0, sz):
                p = choice(rnge)
                while p in dres:
                    p = choice(rnge)
                res.append(p)
                dres[p] = True
            dres = None
        else:
            unused = list()
            used = dict()
            tres = list()
            for i in range(0, sz):
                tres.append(choice(rnge))
            # Sorting out what have been used
            for i in tres:
                # Injecting into results
                if i not in used:
                    res.append(i)
                used[i] = True
            # Stating information about those haven't been used
            for i in rnge:
                if i not in used:
                    unused.append(i)
            # Appending those emptiness...
            used = dict() # To increase performance more greatly
            while len(res) < sz:
                if len(unused) < 1.6 * len(used) and len(used) > 10:
                    # It's time to clear up these indices and it's a log(n) activity
                    unused_new = list()
                    for i in unused:
                        if i not in used:
                            unused_new.append(i)
                    unused = unused_new
                    unused_new = None
                    used = dict() # Clear and make more
                # It's obvious that it became fast enough...
                p = choice(unused)
                while p in used:
                    p = choice(unused)
                res.append(p)
                used[p] = True
    else:
        for i in range(0, sz):
            res.append(choice(rnge))
    return res

def randlist2d(row, column, rnge):
    """This function generates a 2-d list of 'row' rows and 'column'
    columns specified randomly from given set / range 'rnge'. The 'rnge'
    parameter can be specified by anything ranging from 'range' to
    'list', any which could be fit into 'choice' may be available.
    Exempli gratis:
        >>> from pydatagen import *
        >>> my_list = randlist2d(3, 4, range(100, 400))
        >>> my_list
        [[387, 345, 198, 280], [190, 231, 280, 193], [315, 186, 203, 190]]
        >>> print_oi(my_list)
        387 345 198 280
        190 231 280 193
        315 186 203 190
    """
    res = list()
    for i in range(0, row):
        res.append(randlist(column, rnge))
    return res

class UnionFindSet:
    """UnionFindSet provides support for a data structure such union
    and find operations are implemented. Sets may be unioned or
    queried whether two items are in the same set.
    """
    @classmethod
    def find(self, p):
        if p < 1 or p > self.n:
            raise ValueError()
        if self.par[p] == p:
            return p
        self.par[p] = self.find(self.par[p])
        return self.par[p]
    @classmethod
    def union(self, p, q):
        # Literally join p to q (under q)
        p = self.find(p)
        q = self.find(q)
        self.par[p] = q
        return
    @classmethod
    def together(self, p, q):
        return self.find(p) == self.find(q)
    @classmethod
    def __init__(self, n=1):
        self.n = n
        self.par = list()
        for i in range(0, n + 1):
            self.par.append(i)
        return

class Edge:
    """Container for edges in use of Graph and Tree."""
    def __init__(self, u, v, len=None):
        self.u = u
        self.v = v
        self.len = len or 0
        return

class Graph:
    """Basic graph for random generation purposes. When initializing,
    do specify its size of vertexes and edges, and specify its
    characteristics, such as uniformity and whether is a tree.
    Printing support is added by print_oi, which can be found in
    the FUNCTIONS documentation. Exempli gratis:
        >>> from pydatagen import *
        >>> g = Graph(6, 12, connected=True, weighed=True, weight_range=range(10, 99))
        >>> print_oi(g)
        6 12
        2 3 62
        3 1 43
        6 2 70
        4 6 69
        5 4 48
        2 5 68
        6 5 92
        3 6 31
        2 4 98
        4 3 81
        6 1 69
        5 1 55
    """
    def get_edges(self):
        """Returns the list of edges of the graph."""
        return self.edges or list()
    def __try_make_tree(self):
        idx = UnionFindSet(self.n)
        l_n = list(range(1, self.n + 1))
        l_y = list()
        for i in range(1, self.n):
            while True:
                p = choice(l_n)
                q = randrange(1, self.n + 1)
                if not idx.together(p, q) and p != q:
                    break
                continue
            # Create union relationship
            idx.union(p, q)
            # Index the joined nodes
            l_y.append(p)
            if not q in l_y: l_y.append(q)
            l_n.remove(p)
            if q in l_n: l_n.remove(q)
            # Insert into main structure
            ed = Edge(p, q, choice(self.weight_range)) if self.weighed else Edge(p, q)
            self.edges.append(ed)
        return
    def __try_make_graph(self, count):
        for i in range(0, count):
            while True:
                p = randrange(1, self.n + 1)
                q = randrange(1, self.n + 1)
                proper = (p != q)
                for ed in self.edges:
                    if ed.u == p and ed.v == q:
                        proper = False
                        break
                    if ed.v == p and ed.u == q:
                        proper = False
                        break
                if not proper: continue
                break
            ed = Edge(p, q, choice(self.weight_range)) if self.weighed else Edge(p, q)
            self.edges.append(ed)
        return
    def __init__(self, n=1, m=1, **kwargs):
        self.connected = 'connected' in kwargs and kwargs['connected']
        self.weighed = 'weighed' in kwargs and kwargs['weighed']
        if self.weighed:
            self.weight_range = kwargs['weight_range'] or None
        self.edges = list()
        self.n = n
        self.m = m
        if self.connected:
            # This would ignore the 'istree' parameter.
            self.__try_make_tree()
            if m >= n:
                self.__try_make_graph(m - (n - 1))
        else:
            # Does not gurantee connexion.
            self.__try_make_graph(m)
        return

class Tree:
    """Basic tree for random generation purposes. When initializing, do
    specify its size of vertexes, and specify its characteristics, such
    as the max values of children and the weight range of edges. Printing
    support is added by print_oi, which can be found in the FUNCTIONS
    documentation. Exempli gratis:
        >>> # A test for 3-children tree of 18 nodes
        >>> from pydatagen import *
        >>> t = Tree(18, maxchildren=3, weighed=True,weight_range=range(10, 99))
        >>> print_oi(t)
        18
        1 12 77
        1 15 84
        1 3 31
        12 7 37
        12 10 34
        15 9 37
        15 2 54
        3 5 17
        3 18 52
        3 8 49
        7 13 19
        10 6 39
        10 16 97
        9 14 18
        9 11 94
        9 4 94
        2 17 57
    """
    def get_edges(self):
        """Returns the list of edges of the tree."""
        return self.edges or list()
    def __try_make_tree(self):
        import queue
        l_n = list(range(1, self.n + 1))
        l_y = list()
        self.root = randrange(1, self.n + 1)
        que = queue.Queue()
        que.put(self.root)
        l_n.remove(self.root)
        l_y.append(self.root)
        while not que.empty():
            p = que.get_nowait() # p = que.front()
            if len(l_n) < 1:
                break
            n_ch = randrange(1, min(self.maxchildren, len(l_n)) + 1)
            for i in range(0, n_ch):
                q = choice(l_n)
                l_n.remove(q)
                l_y.append(q)
                que.put(q)
                ed = Edge(p, q, choice(self.weight_range)) if self.weighed else Edge(p, q)
                self.edges.append(ed)
            continue
        return
    def __init__(self, n=1, **kwargs):
        self.maxchildren = kwargs['maxchildren'] if 'maxchildren' in kwargs else 2
        self.weighed = 'weighed' in kwargs and kwargs['weighed']
        if self.weighed:
            self.weight_range = kwargs['weight_range'] or None
        self.edges = list()
        self.n = n
        self.__try_make_tree()
        return
