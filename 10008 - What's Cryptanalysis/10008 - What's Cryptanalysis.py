from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    dic = {chr(65 + i): 0 for i in range(26)}
    while cases:
        line = s.readline().strip().upper()
        for char in line:
            if  65 <= ord(char) <= 90:
                if char not in dic:
                    dic[char] = 1
                else: dic[char] += 1
        cases -= 1

    def second(element):
        return element[1]

    res = sorted(dic.items(), key = second, reverse=True)
    for key, value in res:
        if value > 0: print("%c %d" % (key, value))
main()
