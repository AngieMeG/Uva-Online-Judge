from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    for i in range(1, cases + 1):
        line = list(map(int, s.readline().strip().split()))
        high = line.pop(0)
        line.sort()
        print("Case %d: %d" %(i, line[high//2]))
main()