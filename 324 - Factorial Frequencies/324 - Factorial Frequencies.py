from sys import stdin as s


def main():
    dic = {0:1}
    for i in range(1, 367): dic[i] = dic[i-1] * i
    num = int(s.readline().strip())
    while num:
        dic2 = dict([[i, 0] for i in range(10)])
        temp = str(dic[num])
        for char in temp:
            dic2[int(char)] += 1
        line = "{}! --".format(num)
        for i in range(10):
            line += "\n   (" + str(i) + ")" + str(dic2[i]).rjust(5) if i == 5 or i == 0 else "    (" + str(i) + ")" + str(dic2[i]).rjust(5)
        print(line)
        num = int(s.readline().strip())


main()