from sys import stdin
def dp(x,y):
    global dic,lisx,lisy
    if (x,y) not in dic:
        if x == 0 or y == 0:
            dic[(x,y)] = x+y
        elif lisx[x-1] == lisy[y-1]:
            dic[(x,y)] = dp(x-1,y-1)
        else:
            p1 = 1 + dp(x-1,y-1)
            p2 = 1 + dp(x,y-1)
            p3 = 1 + dp(x-1,y)
            dic[(x,y)] = min(p1,p2,p3)
    return dic[(x,y)]


def main():
    en = stdin.readlines()
    for i in range(0,len(en),2):
        en[i] = en[i].strip().split()
        en[i+1] = en[i+1].strip().split()
        global dic,lisx,lisy
        dic = {}
        lisx  = [str(i) for i in en[i][1]]
        lisy = [str(i) for i in en[i+1][1]]
        x = int(en[i][0]);y = int(en[i+1][0])
        print(dp(x,y))
    
    
main()
