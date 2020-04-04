#!/usr/bin/env python3
import sys
sys.path.append("../picklejar3")
from picklejar import PickleJar


pj = PickleJar()
pj.init("bob.pickle", 3)

for i in range(9):
    pj.push("a", i)

pj.push("b", 3.33)
pj.push("d", -1200)

pj.close()

pj.read("bob.pickle")
print(pj.buffer)
