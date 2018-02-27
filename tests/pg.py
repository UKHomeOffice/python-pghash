import random

import string

uc = string.uppercase
lc = string.lowercase
nd = string.digits
pc = "!#%&'()*+,-./:;<=>?@^_`{|}~"

cc = (uc,lc,nd,pc)

type_uc = 0
type_lc = 1
type_nd = 2
type_pc = 3

print uc
print lc
print nd
print pc

pw = ""
type = type_pc

for i in range(1,10):
    roll = random.random()
    if type == type_pc:
        if roll < 0.5:
            type = type_uc
        elif roll < 0.8:
            type = type_lc
        elif roll < 0.9:
            type = type_nd
        else:
            type = type_pc
    elif type == type_uc:
        if roll < 0.2:
            type = type_uc
        elif roll < 0.8:
            type = type_lc
        elif roll < 0.9:
            type = type_nd
        else:
            type = type_pc
    elif type == type_lc:
        if roll < 0.2:
            type = type_uc
        elif roll < 0.8:
            type = type_lc
        elif roll < 0.9:
            type = type_nd
        else:
            type = type_pc
    else:
        if roll < 0.2:
            type = type_uc
        elif roll < 0.5:
            type = type_lc
        elif roll < 0.9:
            type = type_nd
        else:
            type = type_pc
    pw += random.choice(cc[type])

print pw
