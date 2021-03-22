def check_edge(X, graph):
    # use dict to store the adjacency list
    # where first element for the destination vertex
    # second element for the travelling cost
    for v in X:
        for edge in graph[v]:
            if edge[0] not in X:
                return True
    return False

def dijkstra(graph, start):
    # X to store the vertex already explored
    # g_len for their distance to the start
    X, g_len = [start], {}
    for vertex in graph:
        if vertex==X[0]:
            g_len[vertex] = 0
        else:
            g_len[vertex] = float('inf')
    # add new vertex to X
    # by finding the shortest overall distance
    while check_edge(X, graph):
        dist = float('inf')
        for v in X:
            for edge in graph[v]:
                if edge[0] not in X and g_len[v] + edge[1] < dist:
                    w, dist = edge[0], g_len[v] + edge[1] 
        X.append(w)
        g_len[w] = dist
    return g_len

graph = {}
graph['s'] = [['v', 1], ['w', 4]]
graph['v'] = [['w', 2], ['u', 6]]
graph['u'] = [['v', 1], ['t', 6]]
graph['w'] = [['t', 3]]
graph['t'] = []
print('graph 1 is: ')
for vertex in graph:
    print(vertex, ': ', graph[vertex])
print('shortest path from s is: ', dijkstra(graph, 's'), '\n')