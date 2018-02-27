from __future__ import division
import random
from collections import defaultdict

import pghash

results = defaultdict(int)

seed = random.random()

pg=pghash.pghgen(seed=seed)

rolls = 1000000

for i in range(0,rolls):
    r = pg.hash((i,)).random()
    if r < 0.0001:
        results[0.0001]+=1
    elif r < 0.0011:
        results[0.0011]+=1
    elif r < 0.0111:
        results[0.0111]+=1

for k in sorted(results.keys()):
    print "%s, %s, %s"%(k, results[k], results[k]/rolls)

print

results = defaultdict(int)

for i in range(0,rolls):
    r = pghash.pghash((i,)).random()
    if r < 0.0001:
        results[0.0001]+=1
    elif r < 0.0011:
        results[0.0011]+=1
    elif r < 0.0111:
        results[0.0111]+=1

for k in sorted(results.keys()):
    print "%s, %s, %s"%(k, results[k], results[k]/rolls)
