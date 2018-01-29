Procedural Generation with Hashing
==================================

The pghash module is a replacement for some of the main functions in the
random module, but using a hash mechanism instead of random numbers. Rather
than relying on setting a seed and calling the Random object over and over
to generate numbers, pghash takes a distinct tuple for every "random" number
you need.

Usage
-----

Detailed usage information is in pghash/__init__.py

Dependencies
------------

None - earlier versions required xxhash but this is no longer the case.

Discussion
----------

Public discusson can be found on `python-forum.io <https://python-forum.io/Thread-Module-for-procedural-generation-with-hashes>`__.
