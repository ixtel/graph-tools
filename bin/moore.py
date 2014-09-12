#!/usr/bin/env python

"""
Usage:
    $ geng -qc 4 | moore.py
    C~
"""

from sys import stdin

from networkx import is_connected
from networkx import parse_graph6

from igraph import Graph

def moore_order(d, k):
    """
    The maximum number of vertices in a k-regular graph of diameter d.
    """
    return 1 + k*sum([(k - 1)**i for i in range(d)])

def moore_gd(G):
    """
    Decide if G is a Moore graph or not, based on girth and diameter.
    """
    return G.girth() == 2*G.diameter() + 1

def moore_nd(G):
    """
    Decide if G is a Moore graph or not, based on order and diameter.
    """
    return G.vcount() == moore_order(G.diameter(), max(G.degree()))

def moore_gn(G):
    """
    Decide if iG is a Moore graph or not, based on order and girth.
    """
    return G.vcount() == moore_order((G.girth() - 1)/2, min(G.degree()))

if __name__=="__main__":
    for line in stdin.readlines():
        stripped_line = line.rstrip()
        g = parse_graph6(stripped_line)
        G = Graph(edges = g.edges())
        moore = moore_gn
        if moore(G):
            print stripped_line
