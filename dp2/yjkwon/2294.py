# 2294 동전 2
import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]

dp = [float("inf")] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) if dp[k] != float("inf") else print(-1)

"""
f(0) ->  -> 1
f(1) -> 1 -> 1
f(2) -> 1, 1 -> 2
f(3) -> 1, 1, 1, -> 3
f(4) -> 1, 1, 1, 1 -> 4
f(5) -> 1, 1, 1, 1, 1 / 5 -> 1
f(6) -> 1, 1, 1, 1, 1, 1 / 1, 5 -> 2
f(7) -> 1, 1, 1, 1, 1, 1, 1 / 1, 1, 5 -> 3
f(8) -> 1, 1, 1, 1, 1, 1, 1, 1 / 1, 1, 1, 5 -> 4
f(9) -> 1, 1, 1, 1, 1, 1, 1, 1, 1 / 1, 1, 1, 1, 5 -> 5
f(10) -> 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 / 1, 1, 1, 1, 1, 5 / 5, 5 -> 2
f(11) -> 1 * 11 / 1 * 6, 5 / 1, 5, 5 -> 3
f(12) -> 1 * 12 / 1 * 7, 5 / 1, 1, 5, 5 / 12 -> 1
f(13) -> 1 * 13 / 1 * 8, 5 / 1, 1, 1, 5, 5 / 1, 12 -> 2
f(14) -> 1 * 14 / 1 * 9, 5 / 1 * 4, 5, 5 / 1, 1, 12 -> 3
f(15) -> 1 * 15 / 1 * 10, 5 / 5, 5, 5 / 1, 1, 1, 12 -> 3
"""
