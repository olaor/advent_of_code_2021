#!/usr/bin/env python

import sys

school = [ int(x) for x in open(sys.argv[1]).readline().strip().split(',') ]

days = int(sys.argv[2])

new = []

for day in range(days):
    i = 0
    for fish in school:
        if fish == 0:
            school[i] = 6
            new.append(8)
        else:
            school[i] = fish - 1
        i += 1

    school += new
    new = []

print("Number of fish:", len(school))
