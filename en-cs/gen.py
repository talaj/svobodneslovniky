#!/usr/bin/env python

import sys

column_count = 5
line_number = 0
last_pre = None
pre_file = None
index = open('dict/index.js', 'w')
index.write('var index = {\n')

for line in sys.stdin:
    line_number += 1
    entry = line.rstrip('\n').split('\t')
    if len(entry) != column_count:
        raise RuntimeError('Format error on line {}: "{}"'.format(line_number, line))
    en = entry[0]
    pre = en[0:min(2, len(en))]
    pre = pre.lower()
    if pre != last_pre:
        if pre_file:
            pre_file.close()
        name = '.'.join(map(str, map(ord, pre)))
        pre_file = open('dict/' + name, 'w')
        index.write('"{}": "{}",\n'.format(pre, name))
        last_pre = pre
    pre_file.write('\t'.join(entry[0:2]))
    pre_file.write('\n')

if pre_file:
    pre_file.close()
index.write('};\n')
index.close()



#for entry in entries:
    #print('\t'.join(entry))
