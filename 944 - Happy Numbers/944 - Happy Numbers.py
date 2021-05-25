from sys import stdin as s
def isHappy(num):
    global dic
    if num not in dic:
        dic[num] = {num}
        suma = 0
        for i in str(num):
            suma += int(i)**2
        dic[num] = dic[num].union({suma}.union(isHappy(suma)))
    return dic[num]


def main():
    global dic
    dic = {1: {1}}
    line = s.readline().strip()
    while line != "":
        line = line.split(" ")
        for i in range(int(line[0]), int(line[1]) + 1):
            set = isHappy(i)
            if 1 in set:
                print(str(i) + " " + str(len(set)))
        line = s.readline().strip()
        if (line != ""): print()
main()
