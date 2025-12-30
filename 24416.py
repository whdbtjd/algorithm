n = int(input())

dp = [0] * (n + 1)
dp[1] = dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

fib_cnt = dp[n]
fibo_cnt = n - 2

print(fib_cnt, fibo_cnt)
