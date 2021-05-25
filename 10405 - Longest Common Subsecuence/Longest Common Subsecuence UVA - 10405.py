from sys import stdin as s

def main():
    while True:
        try:
            x = input().strip()
            y = input().strip()
            n, m = len(x), len(y)
            dp = [[None for i in range (n+1)] for k in range (m+1)]
            for i in range (m+1):
                for k in range (n+1):
                    if i == 0 or k == 0:
                        dp[i][k] = 0
                    elif x[k-1] != y[i-1]:
                        dp[i][k] = max(dp[i-1][k], dp[i][k-1])
                    else:
                        dp[i][k] = 1 + dp[i-1][k-1]
            print(dp[m][n])
        except:
            break
main()
