from sys import stdin as s

def main():
    line = list(map(int, s.readline().strip().split()))
    while line[0] != 0 and line[1] != 0:
        set1 = set(())
        set2 = set(())
        for i in range(line[0]):
            set1.add(s.readline().strip())
        for i in range(line[1]):
            set2.add(s.readline().strip())
        print(len(set1.intersection(set2)))
        line = list(map(int, s.readline().strip().split()))


main()