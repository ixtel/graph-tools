#!/usr/bin/env python

"""
Usage:
    $ geng -qc 4 | diameter.py
    2
    3
    2
    2
    2
    1
"""

from sys import stdin

from networkx import parse_graph6

from igraph import Graph

if __name__=="__main__":
    for line in stdin.readlines():
        stripped_line = line.rstrip()
        g = parse_graph6(stripped_line)
        G = Graph(edges = g.edges())
        print G.diameter()
