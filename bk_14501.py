import sys

n = int(input())

list_T = [0]*(n+1)
list_P = [0]*(n+1)
dp = [0]*(n+1)
dp.append(0)

for i in range(1, n+1):
    a, b = map(int, sys.stdin.readline().split())
    list_T[i] = a
    list_P[i] = b


for i in range(n, 0, -1):
    if ((n-i+1) < list_T[i]):
        dp[i] = dp[i+1]
    else:
        if ((list_P[i] + dp[i+list_T[i]]) > dp[i+1]):
            dp[i] = list_P[i]+dp[i+list_T[i]]
        else:
            dp[i] = dp[i+1]

print(dp[1])
