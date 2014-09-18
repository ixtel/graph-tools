def colour_edge(G, e, colour):
    G.edge[e[0]][e[1]]['colour'] = colour

def choice_mono(G, e, palette):
    return palette[0]

def used_at(G, u):
    return set([G.edge[u][w].get('colour') for w in G.neighbors(u)])

def choice_greedy(G, e, palette):
    used_colours = used_at(G, e[0]).union(used_at(G, e[1]))
    available_colours = set(palette).difference(used_colours)
    return available_colours.pop()
    
def edge_colouring(G, choice = choice_greedy):
    num_of_edges = len(G.edges())
    max_degree = max(G.degree().values())
    palette = range(0, 2*max_degree)
    for e in G.edges():
        colour_edge(G, e, choice(G, e, palette))

def is_proper_edge(G):
    for u in G.node:
        colours_at_u = []
        for v in G.neighbors(u):
            colours_at_u.append(G.edge[u][v]['colour'])
        if len(set(colours_at_u)) != G.degree(u):
            return False
    return True


