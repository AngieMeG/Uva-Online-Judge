from sys import stdin as s
def main():
    dic = {0:1,1:1}
    for i in range(2, 1001):dic[i] = i * dic[i-1]
    line = s.readline().strip()
    while line:
        line = int(line)
        print("%d!\n%d" % (line, dic[line]))
        line = s.readline().strip()
main()