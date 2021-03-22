def update(Q, DP_Q_old, end):
    DP_Q_new = DP_Q_old.copy()
    for vertex in DP_Q_new:
        dist = float('inf')
        for edge in Q[vertex]:
            temp = DP_Q_old[edge[0]] + edge[1]
            if temp < dist:
                dist = temp
        DP_Q_new[vertex] = dist
    DP_Q_new[end] = 0
    return DP_Q_new

def diff(DP_Q_old, DP_Q_new):
    res = 0
    for vertex in DP_Q_new:
        if DP_Q_new[vertex]==DP_Q_old[vertex]:
            pass
        else:
            res += abs(DP_Q_new[vertex]-DP_Q_old[vertex])
    return res

def DP(Q, end):
    DP_Q_new = {}
    for vertex in Q:
        DP_Q_new[vertex] = 0 if vertex == end else float('inf')
    
    diff_DP = float('inf')
    while diff_DP>1e-8:
        DP_Q_old = DP_Q_new.copy()
        DP_Q_new = update(Q, DP_Q_old, end)
        diff_DP  = diff(DP_Q_old, DP_Q_new)
    return DP_Q_new

Q = {}
infile = open('graph.txt')
for line in infile:
    elements = line.split(',')
    node = elements.pop(0)
    node = int(node[4:])    # convert node description to integer
    Q[node] = []
    for element in elements:
        
        try:
            destination, cost = element.split()
            destination = int(destination[4:])
            Q[node].append([destination, float(cost)])
        except:
            pass
infile.close()
print('graph 2 is: ')
for vertex in Q:
    print(vertex, ': ', Q[vertex])
print('shortest distance to 99 is: ')
DP_Q_new = DP(Q, 99)
for vertex in Q:
    print(vertex, ': ', DP_Q_new[vertex])