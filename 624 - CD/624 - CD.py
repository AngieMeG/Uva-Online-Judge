from sys import stdin as s


def back(total, step, path):
    if total > maxi: return
    if step == size:
        if total >= res[0]:
            res[0] = sum(path)
            res[1] = list(path)
        return
    back(total, step + 1, path)
    back(total + line[step], step + 1, path + [line[step]])


line = list(map(int, s.readline().strip().split()))
while line:
    maxi, size = line[0], line[1]
    line = line[2:]
    res = [0, 0]
    back(0, 0, [])
    print(" ".join(map(str, res[1])), "sum:%d" % (res[0]))
    line = list(map(int, s.readline().strip().split()))
