#!/usr/bin/env python

import sys
import math

column_count = 5
line_number = 0
entries = []

for line in open("en-cs.txt"):
    line_number += 1
    entry = line.rstrip('\n').split('\t')
    if len(entry) != column_count:
        raise RuntimeError('Format error on line {}: "{}"'.format(line_number, line))
    key = entry[0]
    if not entries or entries[-1][0][0] != key:
        entries.append([])
    entries[-1].append(entry)

chunk_size = 500
chunks = [entries[i * chunk_size:i * chunk_size + chunk_size] for i in range(math.ceil(len(entries) / chunk_size))]

keys = [chunk[0][0][0] for chunk in chunks]

#for entry in entries:
    #print('\t'.join(entry))
