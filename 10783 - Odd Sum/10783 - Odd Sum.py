from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    cont = 1
    dic = {1:1, 0:0}
    for i in range(3, 101, 2):
        dic[i] = dic[i - 2] + i
    while cases:
        a = int(input())
        a = a + 1 if a % 2 == 0 and a != 0 else a
        a = 0 if a == 1 or a == 0 else a - 2
        b = int(input())
        b = b - 1 if b % 2 == 0 and b != 0 else b
        print("Case %d: %d" % (cont, dic[b] - dic[a]))
        cases-=1; cont +=1
main()