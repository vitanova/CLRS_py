G = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E'],
    'S' : ['G']
}

def BFS(G, v):
    queue, discovered = [], []
    discovered.append(v)
    queue.append(v)
    while queue:
        v = queue.pop(0)
        for vv in G[v]:
            if vv not in discovered:
                discovered.append(vv)
                queue.append(vv)
    return discovered

def DFS_iter(G, v):
    discovered.append(v)
    for vv in G[v]:
        if vv not in discovered:
            DFS_iter(G, vv)
            
def DFS(G, v):
    global discovered
    discovered = []
    DFS_iter(G, v)
    return discovered

v = 'A'
print('BFS for '+v+' is', BFS(graph, v))
print('DFS for '+v+' is', DFS(graph, v))

import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.DiGraph(G)
nx.draw(G1, with_labels=True, font_weight='bold')