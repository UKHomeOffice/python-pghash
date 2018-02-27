import pghash
import random

pg=pghash.pghgen()

outFile = open("pghash_bytes", "wb")

for x in range(0,1000000):
    char=pg.hash((x,)).randint(0,255)
    hexx=chr(char)
    outFile.write(hexx)

outFile.close()

print "pghash_bytes done"

outFile = open("random_bytes", "wb")

for x in range(0,1000000):
    char=random.randint(0,255)
    hexx=chr(char)
    outFile.write(hexx)

outFile.close()

print "random_bytes done"
