from sys import stdin as s
from math import sqrt

def main():
    print("PERFECTION OUTPUT")
    while True:
        flag = False
        numbers = list(map(int, s.readline().strip().split()))
        for number in numbers:
            if number == 0:
                flag = True
                break
            divs = 0
            root = int()
            res = "DEFICIENT"
            for i in range(1, number):
                if (number % i == 0): divs += i
            if (divs == number): res = "PERFECT"
            elif (divs > number): res = "ABUNDANT"
            print("{:>5}  ".format(number) + res)
        if flag:
            break
    print("END OF OUTPUT")
main()
