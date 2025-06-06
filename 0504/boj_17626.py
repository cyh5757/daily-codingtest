# #DP
# # N을 제곱수들의 합으로 표현
# # 유사 문제 : https://www.acmicpc.net/problem/1699
n = int(input())
dp = [4] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])
