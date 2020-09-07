from sys import stdin as s


def main():
    n = s.readline().strip()
    while n:
        p = int(s.readline().strip())
        print(round(p ** (1 / int(n))))
        n = s.readline().strip()


main()
