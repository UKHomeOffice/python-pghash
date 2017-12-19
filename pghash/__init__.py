"""pghrng - Procedural Generation with Hashes, Random Number Generation

Replacement for the random module which uses hashes instead of (pseudo-)random number generation

Where you would do this:
    rng = random.Random(seed=123)
    age = randint(1,100)

instead do this:
    age_attr = 1
    pgh = pghash.pghgen(seed=123).hash
    age = pgh((age_attr)).randint(1,100)

The pghgen class stores the seed and provides a function that generates a pghash object from a
tuple. The pghash object can then be used to provide a "random" number that conforms to one of
the distributions supported (as per the random module functions random, randint, gauss and choice).

Everything needs a unique tuple (or list). The tuple defines the attribute that you are generating.
If you only want one of the attribute per random seed, you only need one entry in the tuple.

Lets say you want to generate an age, a forename, and a surname for a random number of people.

With random, you might structure the code like this:

    rng = random.Random()
    rng.seed(123)
    num_people = rng.randint(1,100)
    people = [dict() for x in rng.range(num_people)]
    for person in people:
        person['surname'] = rng.choice(surname_list)
        person['forename'] = rng.choice(forename_list)

With pghash, you might do this:

    h1_peoplecount=1
    h1_people=2
    h3_surname=1
    h3_forename=2
    pgh = pghash.pghgen(seed=123).hash
    num_people = pgh((h1_peoplecount)).randint(1,100)
    people = [dict() for x in range(num_people)]
    for h2_index, person in enumerate(people,1):
        person['surname'] = pgh((h1_people,h2_index,h3_surname)).choice(surname_list)
        person['forename'] = pgh((h1_people,h2_index,h3_forename)).choice(forename_list)

You could then introduce a new attribute without disturbing any others:

    h3_midname=3
    ...
    for h2_index, person in enumerate(people,1):
        person['surname'] = pg.h((h1_people,h2_index,h3_surname)).choice(surname_list)
        person['midname'] = pg.h((h1_people,h2_index,h3_midname)).choice(forename_list)
        person['forename'] = pg.h((h1_people,h2_index,h3_forename)).choice(forename_list)

Because each attribute has a unique tuple, it is generated differently from every other attribute
but is repeatable as it is identical each time. The tuple is hashed with the seed to produce a
pseudo-random result.

Changing the seed will, obviously, change the values generated by the hashing. Changing the tuple
stringification will also do this, so make your choice wisely. If your tuples might contain commas,
then don't use comma as the separator. Pick a character or string that will never ever appear in
your tuples. Or, accept that your generated data will totally change if you change the seperator.

    pgh1 = pghash.pghgen(seed=123,joiner='{;}').hash
    pgh2 = pghash.pghgen(seed=123,joiner=('{{','::','}}').hash

"""
from pghash import pghgen, pghash

VERSION = '0.0.2'
__all__ = ['pghgen', 'pghash', 'VERSION']
