from __future__ import division

__version__ = '0.0.3'
__author__ = 'Phil Hibbs'

import md5
from math import sqrt, log, sin, cos, pi
import types

TAU = 2.0*pi

def gaussian(value1, value2):
    """
    Converts two flat distributed numbers into a gaussian distribution
    Input from 0-1, output mean 0 STDDEV 1.
    """
    output1 = sqrt(-2*log(value1))*cos(TAU*value2)
    output2 = sqrt(-2*log(value1))*sin(TAU*value2)
    return output1, output2

class pghgen(object):
    """
    Stores a seed and a separator, and provides a function
    that creates pghash objects from tuples.
    """
    def __init__(self, joiner=lambda t: str(t), seed=0):
        self.seed = seed
        if type(joiner) is types.LambdaType:
            self.joiner = joiner
        else: # If it's not a lambda, then build a lambda on the assumption that it's a tuple or a three-character string
            f1 = lambda t: joiner[0] + joiner[1].join(map(str, t)) + joiner[2] if hasattr(t, '__iter__') else str(t)
            m1 = lambda t: joiner[1].join(map(f1, t))
            self.joiner = m1

    def hash(self, tup):
        """
        Creates pghash objects from tuples using the stored separator.
        """
        return pghash(tup=(self.seed,tup), joiner=self.joiner)

class pghash(object):
    """
    Hashes a tuple, and provides the answer in a variety of forms
    (hex, float, int, gaussian).
    """
    def __init__(self, tup, joiner=lambda t: str(t)):
        self.hex = md5.new(joiner(tup)).hexdigest()

    def pgvalue(self):
        """
        Returns the full integer value of the hash from 0 to 2^^128-1.
        """
        return int(self.hex, 16)

    def pghalves(self):
        """
        Returns the hash value as hex in two halves.
        """
        return self.hex[:16], self.hex[16:]

    def pgvalues(self):
        """
        Returns the hash value as integers in two halves.
        """
        return int(self.hex[:16], 16), int(self.hex[16:], 16)

    def random(self):
        """
        Returns the hash value as a float between 0 and 1.
        """
        return self.pgvalue() / 2**128

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
        floatpair = (intpair[0]/2**64, intpair[1]/2**64)
        return gaussian(floatpair[0], floatpair[1])[0]*sigma+mu

    def normalvariate(self, mu, sigma):
        """
        Returns the hash value as a number with a mean of mu and a standard deviation of sigma.
        """
        return self.gauss(mu, sigma)

    def choice(self, seq):
        """
        Returns an element picked out of collection using the hash value as a random number.
        """
        return seq[int(self.random() * len(seq))]
