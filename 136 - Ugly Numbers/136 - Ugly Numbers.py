def main():
    lis = [0]*1500
    lis[0] = 1
    f2, f3, f5 = 0, 0, 0
    for i in range (1,1500):
        lis[i] = min(2 * lis[f2], 3 * lis[f3], 5 * lis[f5])
        if lis[i] == 2 * lis[f2]: f2 += 1
        if lis[i] == 3 * lis[f3]: f3 += 1
        if lis[i] == 5 * lis[f5]: f5 += 1
    print("The 1500'th ugly number is %d." % (lis[1499]))


main()
