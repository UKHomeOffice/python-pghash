import pghash

three=('a','b','c')
four=('a','b','c','d')
eight=('a','b','c','d','e','f','g','h')
twelve=('a','b','c','d','e','f','g','h','i','j','k','l')
twentysix=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
many=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z')

hashes=[]
sep=','
m2 = lambda t: sep.join(map(str,t))

def pgtest(tuple,seed=None):
    print tuple
    pg=pghash.pghgen(joiner=m2,seed=seed)
    rng=pg.hash(tuple)
    print m2(tuple)
    print rng.hex
    if rng.hex in hashes:
        print "Duplicate hash!"
    hashes.append(rng.hex)
    print rng.gauss(0,1)
    print rng.gauss(100,10)
    print rng.random()
    print rng.choice(three)
    print rng.choice(four)
    print rng.choice(eight)
    print rng.choice(twelve)
    print rng.choice(twentysix)
    print rng.choice(many)

pgtest(('a','b','c'),seed=123)

pgtest(('a','b','c'),seed=1234)

pgtest(('a','b','c'),seed=12345)

pgtest(('a','b','c','d'),seed=12345)

pgtest(('a',1,2,3),seed=12345)

pgtest(('a',(1,2,3)),seed=12345)

pgtest(('a',(1,2)),seed=12345)

pgtest(('a','b','c'),seed=123) # check that this generates the same hash as the first time

print
print
print

hashes=[]
pg=pghash.pghash

def pgtest2(tuple):
    print tuple
    rng=pg(tuple)
    print rng.hex
    if rng.hex in hashes:
        print "Duplicate hash!"
    hashes.append(rng.hex)
    print rng.gauss(0,1)
    print rng.gauss(100,10)
    print rng.random()
    print rng.choice(three)
    print rng.choice(four)
    print rng.choice(eight)
    print rng.choice(twelve)
    print rng.choice(twentysix)
    print rng.choice(many)

pgtest2(('a','b','c'))

pgtest2(('a','b','c'))

pgtest2(('a','b','c'))

pgtest2(('a','b','c','d'))

pgtest2(('a',1,2,3))

pgtest2(('a',(1,2,3)))

pgtest2(('a',(1,2)))

pgtest2(('a','b','c')) # check that this generates the same hash as the first time
