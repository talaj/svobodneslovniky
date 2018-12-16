#!/usr/bin/env python

import sys
import bisect

index = []
with open("chunks/index") as f:
    for line in f:
        index.append(line.rstrip('\n'))

key = sys.argv[1]

print(index)

i = bisect.bisect_left(index, key)
print(i, index[i])
