from sys import stdin as s
from collections import deque
def BFS(source, target, edges):
    global words, dic
    visited = [False for i in range(len(words))]
    distance = [float("inf") for i in range(len(words))]
    u = dic[source]
    distance[u] = 0
    q = deque()
    q.append(u)
    while q:
        u = q.popleft()
        if words[u] == target:
            print("%s %s %d" % (source, target, distance[u]))
            return
        else:
            if not visited[u]:
                visited[u] = True
                for v in edges[u]:
                    if distance[v] > distance[u] + 1:
                        distance[v] = distance[u] + 1
                        q.append(v)
    return

def build_graph():
    global words
    edges = [[] for i in range (len(words))]
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            mismatch = 0
            if len(words[i]) == len(words[j]):
                for k in range(len(words[i])):
                    if words[i][k] !=  words[j][k]: mismatch += 1
                    if mismatch > 1: break
                if mismatch == 1: edges[i] += [j]; edges[j] += [i]
    return edges

def main():
    #out = sys.stdout
    #sys.stdout = open("out.txt","w")
    global words, dic
    cases = int(s.readline().strip())
    s.readline()
    while cases:
        words = []
        dic = {}
        cont = 0
        while True:
            word = s.readline().strip()
            if word == "*": break
            words += [word]
            dic[word] = cont
            cont += 1
        edges = build_graph()
        while True:
            line = s.readline().strip()
            if line == "": break
            source, target = line.split()
            BFS(source, target, edges)
        if cases != 1: print("")
        cases -= 1
    #sys.stdout = out
main()