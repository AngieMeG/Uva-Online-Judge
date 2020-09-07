from sys import stdin

dic = {1: 1}


def back(num):
    if num not in dic:
        if num % 2 == 1:
            res = 1 + back((3 * num) + 1)
        else:
            res = 1 + back((num // 2))
        dic[num] = res
    return dic[num]


def main():
    en = stdin.readline().split()
    while en:
        a, b = [int(i) for i in en]
        res = - float("inf")
        for j in range(min(a, b), max(b, a) + 1):
            res = max(back(j), res)
        print("{} {} {}".format(a, b, res))
        en = stdin.readline().split()


main()
