from sys import stdin as s
import heapq

def dijkstra(graph,s,t):
    n = len(graph)
    visited = [False for i in range(0,n)]
    d = [float("Inf") for i in range(0,n)]
    q = []
    d[s] = 0
    heapq.heappush(q,(0,s))
    while q:
        distance, u = heapq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in graph[u]:
                if (d[u] + w) < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(q,(d[v],v))
    return d[t]
def main():
    for i in range(int(s.readline().strip())):
        n,m,su,t = [int(x) for x in s.readline().strip().split()]
        graph = [[] for x in range(n)]
        for k in range(0,m):
            u,v,w = [int(x) for x in s.readline().strip().split()]
            graph[u].append((v,w))
            graph[v].append((u,w))
        ans = dijkstra(graph,su,t)
        if ans == float("Inf"):print("Case #%d: unreachable"%(i+1))
        else:print("Case #%d: %d"%(i+1,ans))
            
main()
