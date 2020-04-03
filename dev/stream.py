#!/usr/bin/env python3
import sys
sys.path.append("../picklejar3")
from picklejar import PickleJar


pj = PickleJar()
pj.init("bob.pickle", 3)

for i in range(9):
    pj.push("a", i)
pj.close()

pj.read("bob.pickle")
