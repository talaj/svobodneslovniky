#!/usr/bin/env python

import math
import svobodneslovniky

groups = []

for entry in svobodneslovniky.read(open("en-cs.txt")):
    key = entry[0]
    if not groups or groups[-1][0][0] != key:
        groups.append([])
    groups[-1].append(entry)

chunk_size = 500
chunks = [groups[i * chunk_size:i * chunk_size + chunk_size]
    for i in range(math.ceil(len(groups) / chunk_size))]

with open("chunks/index", "w") as f:
    keys = [chunk[0][0][0] for chunk in chunks]
    f.write('\n'.join(keys))

index = 0
for chunk in chunks:
    with open("chunks/{:03}".format(index), "w") as f:
        for group in chunk:
            for entry in group:
                f.write('\t'.join(entry))
                f.write('\n')
    index += 1
