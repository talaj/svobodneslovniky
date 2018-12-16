#!/usr/bin/env python

import sys
import svobodneslovniky

entries = list(svobodneslovniky.read(sys.stdin))
svobodneslovniky.sort(entries)
svobodneslovniky.write(entries, sys.stdout)

