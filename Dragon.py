n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    best = 0
    for k in range(1, 8):  # от 1 до 7 голов
        if i - k >= 0:
            best = max(best, dp[i - k] * k)
    dp[i] = best

print(dp[n])