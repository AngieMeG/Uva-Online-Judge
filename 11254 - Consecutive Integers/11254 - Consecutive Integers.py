""" (+i| a <= i <= b : i) = (a+b)n/2

     Where n is the number of numbers in the secuence
     So b = a + (n-1)

     (+i| a <= i <= a + (n-1) : i) = (2a+ (n-1))n/2
"""

from sys import stdin as s
from math import sqrt
from time import time
def main():
    suma = int(s.readline().strip())
    maxi = []
    while suma + 1:
        ti = time()
        a, b = -1, -1
        for i in range(int(sqrt(2 * suma)), 0, -1):
            a = (2 * suma + i - i**2)/(2 * i)
            if a.is_integer():b = a + i - 1; break
        print("%d = %d + ... + %d" % (suma, a, b))
        maxi += [time()-ti]
        suma = int(s.readline().strip())
    print(max(maxi))
main()
