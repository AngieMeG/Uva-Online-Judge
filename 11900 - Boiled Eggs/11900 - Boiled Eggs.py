from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    cont = 0
    while cases:
        cont += 1
        n,p,q = list(map(int, s.readline().strip().split()))
        eggs = list(map(int, s.readline().strip().split()))
        count = 0
        weight = 0
        for value in eggs:
            if weight + value <= q and count + 1 <= p:
                weight += value
                count += 1
            else: break
        print("Case %d: %d" %(cont, count))
        cases -= 1
main()