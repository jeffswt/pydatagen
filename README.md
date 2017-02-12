
# pydatagen

  > Create random data easier with pydatagen.

Now you can use Python to generate random data for OI problems, in a really
Pythonified way!

## Ports

You can use `printf` just like the way you use it on Codeforces, USACO, BZOJ and
pretty much every Online Judge. It's just that simple, only the fancy formats
are ignored in this version.

If you want to print something, simply write:

```Python
printf("%d %d\n", n, m);
```

The simple applications are really of no differences with C++.

**We are currently working on the porting of `scanf`.**

## Random Generator

We provide two generators, one is called `rand` and the other `xrand`. The only
difference between the two is, when the same function is called regularly,
`xrand` functions 10x faster than `rand`.

For instance, the two snippets of code functions exactly the same:

```Python
for i in range(0, 10000000):
    rand(int, 64, 128)
```

And the optimized version as follows:

```Python
g = xrand(int, 64, 128)
for i in range(0, 10000000):
    next(g)
```

Detailed usage of these functions can be referred in the Python interactive
help console by typing `help('pydatagen.rand')`, had you installed this package.

## Installation

Clone the repository into an empty folder, and execute the following command:

```sh
pip install setuptools # If you have already installed this before, ignore it
python setup.py install # Install pydatagen
```

You can also build your Wheel package by executing the following command:

```sh
pip install setuptools # If you have already installed this before, ignore it
pip install wheel # Install bdist_wheel provider
python setup.py build bdist_wheel # Build .whl package
```

Alternatively you could download our official release from the releases panel,
and install the compiled 'wheel' to your computer. After you have downloaded
the release, you may install it in the command line:

```sh
pip install ./pydatagen-version-py3-none-any.whl # Referring to the downloaded file
```

Installation is as fast as creating random data!

## Pros and Cons

The pros of using pydatagen:

  - [x] Easier to write than C++ random generators
  - [x] Shorten your code by 80%
  - [x] Allows more advanced ways of data generation
  - [x] Extensible modules makes adding data type support easier

However, there are a few drawbacks that cannot be avoided at present:

  - [ ] Slow generation speed, around 3x slower than general Python approaches
  - [ ] Way slower than NumPy and C++ implementations

If you don't care much about performance, than we believe that pydatagen is the
best choice you have. It also works well with `pyjudge` and `pyMatcher`.
