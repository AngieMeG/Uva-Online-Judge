from sys import stdin as s


def main():
    cases = int(s.readline())
    while cases:
        dots = int(s.readline())
        pairs = []
        while dots:
            pairs += [list(map(int, s.readline().split()))]
            dots -= 1
        pairs.sort(reverse=True)
        maxi = pairs[0]
        length = 0
        for i in range(1, len(pairs)):
            if pairs[i][1] > maxi[1]:
                dx, dy = pairs[i][0] - pairs[i - 1][0], pairs[i][1] - pairs[i - 1][1]
                total_length = (dx ** 2 + dy ** 2) ** (1 / 2)
                length += (pairs[i][1] - maxi[1]) * total_length / dy
                maxi = pairs[i]
        print("%.2f" % length)
        cases -= 1


main()
