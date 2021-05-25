import bisect as b
from sys import stdin as s
def main():
    while True:
        try:
            int(s.readline())
            prices = []
            for price in list(map(int, s.readline().strip().split())):
                b.insort_left(prices, price)
            ans = []
            money = int(s.readline().strip())
            min_diff = float("inf")
            for i in range(len(prices)-1):
                index = b.bisect_left(prices[i+1:], money - prices[i]) + i + 1
                if index != len(prices) and prices[index] == money - prices[i]:
                    actual = prices[index] - prices[i]
                    if actual < min_diff:
                        min_diff = actual
                        ans = [i, index]
            print("Peter should buy books whose prices are %d and %d." % (prices[ans[0]], prices[ans[1]]))
            print()
            s.readline()
        except Exception:
            break
main()



  