from sys import stdin as s
def main():
    dic = {1:[0,1,0,0,0,0,0,0,0,0]}
    for i in range(2, 10001):
        temp = list(dic[i - 1])
        dic[i] = temp
        for digit in str(i):
            dic[i][int(digit)] += 1
    cases = int(s.readline().strip())
    for i in range(cases):
        num = int(s.readline().strip())
        print(*dic[num])
main()