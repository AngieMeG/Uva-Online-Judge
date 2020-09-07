from sys import stdin as s
import heapq
def djk(s):
    global graph,nodes
    visited = [False]*(nodes+1)
    d = [float("inf")]*(nodes+1)
    q = []
    d[s] = 0
    heapq.heappush(q,(0,s))
    while q:
        distance,u = heapq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v,w in graph[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(q,(d[v],v))
    return d
def main():
    global graph,nodes
    cases = int(s.readline().strip())
    for i in range(cases):
        blank = s.readline().strip()
        if i != 0:print()
        graph = {}
        nodes = int(s.readline().strip())
        exit = int(s.readline().strip())
        time = int(s.readline().strip())
        connections = int(s.readline().strip())
        for j in range(1,nodes+1):
            graph[j] = []
        for j in range(connections):
            a,b,w = [int(x) for x in s.readline().strip().split()]
            graph[b].append((a,w))
        dis = djk(exit)
        res = 0
        for k in dis:
            if k <= time:res+=1
        print(res)

main()