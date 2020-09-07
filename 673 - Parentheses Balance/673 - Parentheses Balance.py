from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    while cases:
        line = s.readline().strip().replace(" ","")
        dic = {"(": ")", "[": "]"}
        lis = []
        res = True
        for char in line:
            if char in dic:
                lis.append(char)
            else:
                if len(lis):
                    sim = lis.pop()
                    if dic[sim] != char: res = False;break
                else:
                    res = False;break
        print("Yes") if res and not lis else print("No")
        cases -= 1


main()
