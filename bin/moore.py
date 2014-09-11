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

def moore(G):
    """
    Decide if G is a Moore graph or not, based on girth and diameter.
    """
    degree = G.degree().values()
    K = max(degree)
    k = min(degree)
    if is_connected(G) and k == K:
      iG = Graph(edges = G.edges())
      return iG.girth() == 2*iG.diameter() + 1

def moore2(G):
    """
    Decide if G is a Moore graph or not, based on order and diameter.
    """
    degree = G.degree().values()
    K = max(degree)
    k = min(degree)
    if is_connected(G) and k == K:
      iG = Graph(edges = G.edges())
      return G.order() == moore_order(iG.diameter(), K)

def moore3(G):
    """
    Decide if G is a Moore graph or not, based on order and girth.
    """
    degree = G.degree().values()
    K = max(degree)
    k = min(degree)
    if is_connected(G) and k == K:
      iG = Graph(edges = G.edges())
      return G.order() == moore_order((iG.girth() - 1)/2, k)

if __name__=="__main__":
    for line in stdin.readlines():
        stripped_line = line.rstrip()
        g = parse_graph6(stripped_line)
        if moore3(g): print stripped_line
