from __future__ import division

__version__ = '0.0.1'
__author__ = 'Phil Hibbs'

import xxhash
from numpy import sqrt, log, sin, cos, pi

def gaussian(value1, value2):
    """
    Converts two flat distributed numbers into a gaussian distribution
    Input from 0-1, output mean 0 STDDEV 1.
    """
    tau = 2*pi
    output1 = sqrt(-2*log(value1))*cos(tau*value2)
    output2 = sqrt(-2*log(value1))*sin(tau*value2)
    return output1, output2

class pghgen(object):
    """
    Stores a seed and a separator, and provides a function
    that creates pghash objects from tuples.
    """
    def __init__(self, seed=0, sep=','):
        self.seed = seed
        self.sep = sep

    def hash(self, tup):
        """
        Creates pghash objects from tuples using the stored seed and separator.
        """
        return pghash(tup=tup, seed=self.seed, sep=self.sep)

class pghash(object):
    """
    Hashes a tuple using a seed, and provides the answer in a variety of forms
    (hex, float, int, gaussian).
    """
    def __init__(self, tup, seed=0, sep=','):
        self.hex = xxhash.xxh64(sep.join(map(str,tup)), seed=seed).hexdigest()

    def pgvalue(self):
        """
        Returns the full integer value of the hash from 0 to 2^^64-1.
        """
        return int(self.hex, 16)

    def pghalves(self):
        """
        Returns the hash value as hex in two halves.
        """
        return self.hex[:8], self.hex[8:]

    def pgvalues(self):
        """
        Returns the hash value as integers in two halves.
        """
        return int(self.hex[:8], 16), int(self.hex[8:], 16)

    def random(self):
        """
        Returns the hash value as a float between 0 and 1.
        """
        return self.pgvalue() / 2**64

    def randint(self, lbound, ubound):
        """
        Returns the hash value as an integer in the range supplied.
        """
        return int(self.random() * (ubound-lbound+1) + lbound)

    def gauss(self, mu, sigma):
        """
        Returns the hash value as a number with a mean of mu and a standard deviation of sigma.
        """
        intpair = self.pgvalues()
        floatpair = (intpair[0]/2**32, intpair[1]/2**32)
        return gaussian(floatpair[0], floatpair[1])[0]*sigma+mu

    def choice(self, collection):
        """
        Returns an element picked out of collection using the hash value as a random number.
        """
        return collection[self.randint(0, len(collection)-1)]
