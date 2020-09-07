from sys import stdin


def LCS(x,y,x1,y1):
    global dic
    if (x1,y1) not in dic:
        if x1 < 0 or y1 < 0:
            dic[(x1,y1)] = 0
        elif x[x1] == y[y1]:
            dic[(x1,y1)] = 1 + LCS(x,y,x1-1,y1-1)
        else:
            p1 = LCS(x,y,x1-1,y1)
            p2 = LCS(x,y,x1,y1-1)
            dic[(x1,y1)] = max(p1,p2)
    return dic[(x1,y1)]
            
            
def main():
    while True:
        try:
            x = stdin.readline().strip()
            y = stdin.readline().strip()
            global dic
            dic = {}
            print(LCS(x,y,len(x)-1,len(y)-1))
        except EOFError: break


main()
