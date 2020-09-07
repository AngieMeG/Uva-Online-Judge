from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    while cases:
        input()
        slots = list(map(int, s.readline().strip().split()))
        slots.sort()
        print((slots[-1]-slots[0])*2)
        cases -= 1
main()