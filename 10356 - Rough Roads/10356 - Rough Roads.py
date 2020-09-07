from sys import stdin as s
import heapq

def djk(s,t):
    global graph
    n = len(graph)
    visited = [False for i in range(500*10+3)]
    d = [float("inf") for i in range(500*10+3)]
    q = []
    #d[even(s)] = 0
    d[s*10+2] = 0
    #heapq.heappush(q,(0,even(s)))
    heapq.heappush(q, (0, s*10+2))
    while q:
        distance, u = heapq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in graph[u]:
                if (d[u] + w) < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(q,(d[v],v))
    #return d[even(t)]
    return d[t*10+2]

def even(x):
    return x*10+2

def odd(x):
    return x*10+1

def addEdge(a, b, cost):
    global graph
    """graph[even(a)].append((odd(b), cost))
    graph[odd(a)].append((even(b), cost))
    graph[even(b)].append((odd(a), cost))
    graph[odd(b)].append((even(a), cost))"""
    graph[a*10+2].append((b*10+1, cost))
    graph[a*10+1].append((b*10+2, cost))
    graph[b*10+2].append((a*10+1, cost))
    graph[b*10+1].append((a*10+2, cost))

def main():
    line = s.readline().strip()
    cont = 1
    while  line:
        nodes, connections = [int(i) for i in line.split()]
        global graph
        graph = {}
        for i in range(0, nodes):
            #graph[even(i)] = []
            #graph[odd(i)] = []
            graph[i*10+2] = []
            graph[i*10+1] = []
        for i in range (connections):
            n1, n2, weight = list(map(int, s.readline().strip().split()))
            addEdge(n1, n2, weight)
        res = djk(0, nodes - 1)
        if res == float("inf"): res = "?"
        print("Set #{}\n{}".format(cont, res))
        cont += 1
        line = s.readline().strip()
main()