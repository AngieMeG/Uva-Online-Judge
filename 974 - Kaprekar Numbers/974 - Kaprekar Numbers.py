from sys import stdin as s

def main():
    cases = int(s.readline().strip())
    dic = {}
    for j in range(1, cases + 1):
        low, high = [int(i) for i in s.readline().strip().split(" ")]
        res = []
        for i in range(low, high+1):
            if i not in dic:
                is_kaprekar = False; value = i; num = str(i ** 2)
                for k in range(1, len(num)):
                    value1 = int(num[0:k]); value2 = int(num[k::])
                    if (value1 and value2) and (value2 + value1 == value): is_kaprekar = True; break
                dic[i] = is_kaprekar
            if dic[i]: res += [str(i)]
        print("case #"+str(j))
        if not len(res):
            print("no kaprekar numbers")
        else:
            print("\n".join(res))
        if j != cases: print("")
main()