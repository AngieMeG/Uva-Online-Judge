from sys import stdin

# Run time error, prob num max recursion
def LCS(x,y,x1,y1):
    global dic
    if (x1,y1) not in dic:
        if x1 < 0 or y1 < 0:
            dic[(x1,y1)] = 0
        elif x[x1] == y[y1]:
            dic[(x1,y1)] = 1 + LCS(x,y,x1-1,y1-1)
        else:
            dic[(x1,y1)] = max(LCS(x,y,x1-1,y1),LCS(x,y,x1,y1-1))
    return dic[(x1,y1)]
            
            
def main():
    global dic
    x = stdin.readline().strip()
    while x != "":
        dic = {}
        y = stdin.readline().strip()
        print(LCS(x, y, len(x)-1, len(y)-1))
        x = stdin.readline().strip()
        
main()
