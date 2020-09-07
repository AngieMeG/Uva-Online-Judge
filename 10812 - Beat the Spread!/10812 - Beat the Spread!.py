from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    while cases:
        sumac, difference = map(int, s.readline().strip().split())
        if difference > sumac or (sumac - difference) % 2 != 0:
            print("impossible")
        else:
            b = (sumac - difference) // 2
            a = difference + b
            print(a, b)
        cases -= 1


main()
