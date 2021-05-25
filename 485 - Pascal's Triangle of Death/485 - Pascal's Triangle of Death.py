dic = {0: [0, 1, 0], 1: [0, 1, 1, 0]}
print(*(dic[0][1:-1])); print(*(dic[1][1:-1]))
i = 2
while True:
    res1 = [0]
    res2 = [0]
    for j in range(1, len(dic[i-1])//2 + 1):
        value = dic[i-1][j] + dic[i-1][j-1]
        res1 += [value]
        res2 = [value] + res2
    res2 = res2 if i % 2 != 0 else res2[1::]
    dic[i] = res1 + res2
    print(*(dic[i][1:-1]))
    i += 1
    if value >= 10**60:
        break