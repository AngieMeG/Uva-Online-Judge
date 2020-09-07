from sys import stdin as s
from math import ceil
def main():
    num = s.readline().strip()
    while num:
        num = int(num)
        value = ceil((- 1 + (1 + 4*2*num)**(1/2))/2)
        numerator = value - (num - 1 - (((value - 1) * value)/2))
        denominator = 1 + (num - 1 - (((value - 1) * value)/2))
        if value % 2 == 0:
            numerator, denominator = denominator, numerator
        print("TERM %d IS %d/%d" %(num, numerator, denominator))
        num = s.readline().strip()
main()