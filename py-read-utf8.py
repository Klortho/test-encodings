#!/usr/bin/env python

with open('static.js') as f:
    for line in f:
        print('"' + line.rstrip('\n') + '"')
f.close()
