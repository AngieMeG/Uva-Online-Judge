from sys import stdin as s
from collections import deque
class Node:
    def __init__(self):
        self.p = self
        self.rank = 0
def find(x):
    if x != x.p:
        x.p = find(x.p)
    return  x.p

def link(x,y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if y.rank == x.rank:
            y.rank += 1

def union(x,y):
    link(find(x),find(y))

def main():
    dic = {}
    for i in range(10):
        var = {}
        for j in range(10):
            var[str(j)] = min(abs(i-j),10-abs(i-j))
        dic[str(i)] = var
    for i in range(int(s.readline().strip())):
        minimo = float("inf")
        line = deque(s.readline().strip().split())
        num = int(line.popleft())
        edges = []
        for j in range(num):
            var = dic["0"][line[j][0]]+dic["0"][line[j][1]]+dic["0"][line[j][2]]+dic["0"][line[j][3]]
            minimo = min(minimo, var)
        for j in range(num):
            p1 = line[j]
            for k in range(j+1,num):
                p2 = line[k]
                w = dic[p1[0]][p2[0]]+dic[p1[1]][p2[1]]+dic[p1[2]][p2[2]]+dic[p1[3]][p2[3]]
                edges.append([w,j,k])
        edges = sorted(edges)
        nodes = [Node() for x in range(num)]
        cont= 1
        total = 0
        for w,u,v in edges:
            node_u = nodes[u]
            node_v = nodes[v]
            if find(node_u) != find(node_v):
                union(node_u,node_v)
                cont += 1
                total += w
                if cont == num:break
        print(total+minimo)
main()
