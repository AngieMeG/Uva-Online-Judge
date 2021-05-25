from sys import stdin as s
import bisect as b

def closest_sum(num, lis):
    min_diff = float("inf")
    actual_sum = float("inf")
    for i in range(len(lis)-1):
        index = b.bisect_left(lis[i+1:], abs(lis[i] - num)) + i + 1
        if index != 0 and index - 1 != i and min_diff > abs(lis[index-1] + lis[i] - num):
            min_diff = abs(lis[index-1] + lis[i] - num)
            actual_sum = lis[index-1] + lis[i]
        if index != len(lis) and min_diff > abs(lis[index] + lis[i] - num):
            min_diff = abs(lis[index] + lis[i] - num)
            actual_sum = lis[index] + lis[i]
    return actual_sum

def main():
    case = int(s.readline().strip())
    cont = 1
    while case != 0:
        lis = []
        for i in range(case):
            b.insort_left(lis, int(s.readline().strip()))
        num_queries =int(s.readline().strip())
        print("Case %d:" %(cont))
        for i in range(num_queries):
            num = int(s.readline().strip())
            print("Closest sum to %d is %d." %(num, closest_sum(num, lis)))
        case = int(s.readline().strip())
        cont += 1
main()