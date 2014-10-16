#!/usr/bin/env python

"""
Usage:
    $ geng -qc 4 | maxdeg.py
    3
    2
    3
    2
    3
    3
"""

from sys import stdin

from networkx import parse_graph6

if __name__=="__main__":
    for line in stdin.readlines():
        stripped_line = line.rstrip()
        g = parse_graph6(stripped_line)
        print max(g.degree().values())
