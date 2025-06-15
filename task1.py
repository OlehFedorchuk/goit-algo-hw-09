from collections import defaultdict
import time

# Номінали монет
COINS = [50, 20, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount):
    result = defaultdict(int)
    for coin in COINS:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    return dict(result)

# Алгоритм динамічного програмування
def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result = defaultdict(int)
    while amount > 0:
        coin = prev[amount]
        result[coin] += 1
        amount -= coin
    return dict(result)

# Тестування
amount = 113

# Жадібний алгоритм
start_greedy = time.time()
greedy_result = find_coins_greedy(amount)
end_greedy = time.time()

# Динамічне програмування
start_dp = time.time()
dp_result = find_min_coins(amount)
end_dp = time.time()

# Вивід результатів
print("Greedy result:", greedy_result)
print("Greedy time:", end_greedy - start_greedy)

print("DP result:", dp_result)
print("DP time:", end_dp - start_dp)
