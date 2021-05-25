from sys import stdin as s
from math import floor as f
def main():
    cases = int(s.readline())
    for i in range(cases):
        warriors = int(s.readline())
        print(f((-1+(1+(8*warriors))**(1/2))/2))
main()