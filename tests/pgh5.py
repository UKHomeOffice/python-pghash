import pghash
import time

seed = 123
mv = 1

pg=pghash.pghgen(seed=seed)

t = time.time()
for x in range(0,1000000):
    mv = min(mv, pg.hash((x,)).random())
print time.time() - t

print mv
