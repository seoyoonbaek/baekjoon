n = int(input())

dp = [[0 for _ in range(10)] for _ in range(1001)]

for i in range(0, 10):
    dp[1][i] = 1


for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][0]
        else:
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]

print(sum(dp[n][0:10]) % 10007)    