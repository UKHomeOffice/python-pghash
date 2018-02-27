import pghash
import string
from collections import defaultdict

f1 = lambda t: '{' + sep.join(map(str, t)) +'}' if hasattr(t, '__iter__') else str(t)
m1 = lambda t: sep.join(map(f1, t))

three=('a','b','c')
four=('a','b','c','d')
eight=('a','b','c','d','e','f','g','h')
twelve=('a','b','c','d','e','f','g','h','i','j','k','l')
twentysix=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
many=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z','z')

results = defaultdict(int)
pg=pghash.pghgen(joiner='{:}')

def pgtest(tuple):
    rng=pg.hash(tuple)
    randint = rng.randint(1,100)
    results[randint] += 1

for c1 in string.ascii_lowercase:
    for c2 in string.ascii_lowercase:
        for c3 in string.ascii_lowercase:
            pgtest((c1,c2,c3))

for k in sorted(results.keys()):
    print k, results[k]
