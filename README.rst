Procedural Generation with Hashing
==================================

The pghash module is a replacement for some of the main functions in the
random module, but using a hash mechanism instead of random numbers. Rather
than relying on setting a seed and calling the Random object over and over
to generate numbers, pghash sets the seed and you pass in a distinct tuple
for every random number you need.

Dependencies
------------

Requires two non-core modules: xxhash and numpy.

xxhash is non-trivial on Windows, as installation requires the Microsoft C++ 
compiler for either `Python 2.7 <https://www.microsoft.com/en-ie/download/details.aspx?id=44266>`__ or `Python 3.0 <https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017>`__.

Discussion
----------

Public discusson can be found on `python-forum.io <https://python-forum.io/Thread-Module-for-procedural-generation-with-hashes>`__.
