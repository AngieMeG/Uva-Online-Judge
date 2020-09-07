from sys import stdin as s


def main():
    factorial = {0: 1}
    for i in range(1, 21): factorial[i] = factorial[i - 1] * i
    cases = int(s.readline().strip())
    for i in range(1, cases + 1):
        letters = dict([[chr(i), 0] for i in range(65, 91)])
        word = s.readline().strip()
        for char in word: letters[char] += 1
        res = factorial[len(word)]
        for key in letters: res /= factorial[letters[key]]
        print("Data set %d: %d" % (i, res))


main()
