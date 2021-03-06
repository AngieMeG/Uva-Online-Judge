from sys import stdin
import math
import heapq
def main():
    cases = int(stdin.readline().strip())
    for case in range(cases):
        stdin.readline()
        n = int(stdin.readline().strip())
        points = []
        for i in range(n):
            x, y = [float(x) for x in stdin.readline().split()]
            points.append((x,y))
        edges = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                p1 = points[i]
                p2 = points[j]
                w = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
                edges[i][j] = w
                edges[j][i] = w
        visited = [False for i in range(n)]
        distances = [float('inf') for i in range(n)]
        s = 0
        distances[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        total = 0.0
        while q:
            d, u = heapq.heappop(q)
            if visited[u] == False:
                visited[u] = True
                total += distances[u]
                for v in range(n):
                    if u != v and visited[v] == False and edges[u][v] < distances[v]:
                        distances[v] = edges[u][v]
                        heapq.heappush(q, (distances[v], v))
        if case != 0:print()
        print('%.2f' % (total))

main()
