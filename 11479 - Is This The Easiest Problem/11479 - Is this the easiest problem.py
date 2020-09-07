from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    cont = 0
    while cases:
        type = "Invalid"
        cont += 1
        a, b, c = list(map(int, s.readline().strip().split()))
        if a <= 0 or b <= 0 or c <= 0: type = "Invalid"
        elif a + b > c and b + c > a  and a + c > b:
            if a == b and b == c: type = "Equilateral"
            elif a != b and b != c and c != a: type = "Scalene"
            else: type = "Isosceles"
        print("Case %d: %s" %(cont, type))
        cases -= 1
main()