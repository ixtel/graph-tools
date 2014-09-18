#!/usr/bin/env python

"""
Usage:
    $ geng -qc 3 | edge_colouring.py
    2
    3
"""

from sys import stdin

from networkx import parse_graph6

def colour_edge(G, e, colour):
    """
    Assign 'colour' to edge 'e' in graph 'G'.
    """
    G.edge[e[0]][e[1]]['colour'] = colour

def choice_mono(G, e, palette):
    """
    A monochromatic colouring strategy.
    """
    return palette[0]

def used_at(G, u):
    """
    Returns the set of all colours on edges incident with u in G.
    """
    return set([G.edge[u][w].get('colour') for w in G.neighbors(u)])

def choice_greedy(G, e, palette):
    """
    A greedy colouring strategy.
    """
    used_colours = used_at(G, e[0]).union(used_at(G, e[1]))
    available_colours = set(palette).difference(used_colours)
    return available_colours.pop()
    
def edge_colouring(G, choice = choice_greedy):
    """
    Visits every edge in G and applies a colour chosen by `choice` strategy.
    """
    max_degree = max(G.degree().values())
    palette = range(0, 2*max_degree)
    for e in G.edges():
        colour_edge(G, e, choice(G, e, palette))

def is_proper_edge(G):
    """
    Decides whether G is properly edge-coloured or not.
    """
    for u in G.node:
        if len(used_at(G, u)) != G.degree(u):
            return False
    return True

def n_colours_edge(G):
    """
    Determines how many colours are used on edges of G.
    """
    colours = []
    for u, v in G.edges():
        colours.append(G.edge[u][v]['colour'])
    return len(set(colours))

if __name__=="__main__":
    for line in stdin.readlines():
        stripped_line = line.rstrip()
        G = parse_graph6(stripped_line)
        edge_colouring(G)
        print n_colours_edge(G)
