from sys import stdin as s
def main():
    num = int(s.readline().strip())
    cont = 1
    while num:
        line = list(map(int,s.readline().strip().split()))
        wall = sum(line)//num
        movs = 0
        for h in line:
            if h > wall:movs += h - wall
        print("Set #%d\nThe minimum number of moves is %d.\n" % (cont,movs))
        cont += 1
        num = int(s.readline().strip())
main()