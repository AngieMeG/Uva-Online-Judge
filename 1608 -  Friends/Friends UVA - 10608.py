from sys import stdin as s
class ds:
    def __init__(self):
        self.p = self
        self.rank = 0
        self.size = 1
def link(x,y):
    if x.rank > y.rank:
        x.size += y.size
        y.p = x
    else:
        x.p = y
        y.size += x.size
        if x.rank == y.rank:
            y.rank += 1 
def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p
def union(x,y):
    link(find_set(x),find_set(y))
def main():
    cases = int(s.readline().strip())
    for i in range (cases):
        n,m = [int(k) for k in s.readline().strip().split()]
        lis =[ds() for k in range(n)]
        for k in range(m):
            a,b = [int(j)-1 for j in s.readline().strip().split()]
            if find_set(lis[a]) != find_set(lis[b]):
                union(lis[a],lis[b])
        ans = 0
        for k in range(len(lis)):
            if lis[k].size > ans:ans = lis[k].size
        print(ans)
main()
