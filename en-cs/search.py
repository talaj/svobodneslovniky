#!/usr/bin/env python

import sys
import bisect
import svobodneslovniky

index = []
with open("chunks/index") as f:
    for line in f:
        index.append(line.rstrip('\n').lower())

def search(chunk, query):
    with open("chunks/{:03}".format(chunk)) as f:
        entries = list(svobodneslovniky.read(f))
        keys = list([entry[0] for entry in entries])
        i = bisect.bisect(keys, query)
        return entries[i:]

for line in sys.stdin:
    query = line.lower()
    chunk = bisect.bisect(index, query)
    entries = search(max(0, chunk - 1), query)
    for entry in entries[:5]:
        print(entry[0], entry[1])
