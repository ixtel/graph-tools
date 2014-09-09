#!/usr/bin/env python

from networkx import is_connected
from networkx import parse_graph6, generate_graph6
from igraph import Graph
from sys import stdin

def cage_order(d, k):
    """Diameter is d. Degree is k."""
    return 1 + k*sum([(k - 1)**i for i in range(d)])

def moore(G):
    K = max(G.degree().values())
    k = min(G.degree().values())
    if k != K or not is_connected(G):
        return False
    else:
        iG = Graph(edges = G.edges())
        return iG.girth() == 2*iG.diameter() + 1

def moore2(G):
    K = max(G.degree().values())
    k = min(G.degree().values())
    if k != K or not is_connected(G):
        return False
    else:
        iG = Graph(edges = G.edges())
        return G.order() == cage_order(iG.diameter(), K)

def moore3(G):
    K = max(G.degree().values())
    k = min(G.degree().values())
    if k != K or not is_connected(G):
        return False
    else:
        iG = Graph(edges = G.edges())
        return G.order() == cage_order((iG.girth() - 1)/2, k)

if __name__=="__main__":
    for line in stdin.readlines():
        g = parse_graph6(line.rstrip())
        if moore(g):
            print generate_graph6(g, header = False)
