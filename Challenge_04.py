def count_payment_combinations(coins, total_sum):
    n = len(coins)
    dp = [0] * (total_sum + 1)
    dp[0] = 1  # base case: one way to make sum 0

    for coin in coins:
        for s in range(coin, total_sum + 1):
            dp[s] += dp[s - coin]

    return dp[total_sum]


coins = [1, 2, 3]
total_sum1 = 4
total_sum2 = 5

print(count_payment_combinations(coins, total_sum1))  # Expected: 4 ([1,1,1,1],[1,1,2],[1,3],[2,2])
print(count_payment_combinations(coins, total_sum2))  # Expected: 5 ([1,1,1,1,1],[1,1,3],[1,2,2],[2,3],[1,1,1,2])
