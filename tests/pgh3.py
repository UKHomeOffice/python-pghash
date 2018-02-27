import pghash
import string
from collections import defaultdict

results = defaultdict(int)

pg=pghash.pghgen()

for c1 in string.ascii_lowercase:
    for c2 in string.ascii_lowercase:
        for c3 in string.ascii_lowercase:
            for c4 in string.ascii_lowercase:
                rv = pg.hash((c1,c2,c3,c4)).gauss(100,10)
                results[round(rv,0)] += 1

for k in sorted(results.keys()):
    print "%d,%d"%(k, results[k])

results = defaultdict(int)

pg=pghash.pghash

for c1 in string.ascii_lowercase:
    for c2 in string.ascii_lowercase:
        for c3 in string.ascii_lowercase:
            for c4 in string.ascii_lowercase:
                rv = pg((c1,c2,c3,c4)).gauss(100,10)
                results[round(rv,0)] += 1

for k in sorted(results.keys()):
    print "%d,%d"%(k, results[k])
