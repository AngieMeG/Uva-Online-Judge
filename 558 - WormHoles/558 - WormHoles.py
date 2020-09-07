from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    rta = ""
    for i in range(cases):
        systems, num = [int(i) for i in s.readline().strip().split()]
        di = [float("Inf")]*systems
        di[0] = 0
        graph = []
        for k in range(num):
            ite = [int(i) for i in s.readline().strip().split()]
            graph += [ite]
        for k in range(systems-1):
            for u,v,w in graph:
                if di[u] != float("Inf") and di[u] + w < di[v]:
                    di[v] = di[u] + w
        res = "not possible\n"
        for u,v,w in graph:
            if di[u] != float("Inf") and di[u] + w < di[v]:
                res = "possible\n"
                break
        rta += res
    print(rta.strip())
    
main()
