from sys import stdin as s
import math
def main():
    dic = {1: 0}
    i = 2
    while i**2 < 100490:
        dic[i**2] = dic[(i-1)**2] + 1
        i +=1
    a,b = list(map(int, s.readline().strip().split()))
    while a and b:
        a = math.ceil(a ** (1 / 2)) ** 2
        b = (math.floor(b**(1/2))+1)**2
        print(dic[b] - dic[a])
        a, b = list(map(int, s.readline().strip().split()))
main()