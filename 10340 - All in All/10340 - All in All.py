from sys import stdin as y


def main():
    line = y.readline().strip()
    while line:
        s, t = line.split()
        sizes, sizet = len(s), len(t)
        ps = 0
        for i in range(sizet):
            if s[ps] == t[i]: ps += 1
        print("Yes") if ps == sizes else print("No")
        line = y.readline().strip()


main()