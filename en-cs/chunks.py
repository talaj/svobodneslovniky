#!/usr/bin/env python

import math
import svobodneslovniky

entries = list(svobodneslovniky.read(open("en-cs.txt")))

chunk_size = 500
chunks = [entries[i * chunk_size:i * chunk_size + chunk_size]
    for i in range(math.ceil(len(entries) / chunk_size))]

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
