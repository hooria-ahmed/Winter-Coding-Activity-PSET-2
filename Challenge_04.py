def count_payment_combinations(coins, total_sum):
    def helper(index, remaining_sum):
        if remaining_sum == 0:
            return 1
        if remaining_sum < 0 or index == len(coins):
            return 0

        # Choice 1: take the coin
        take = helper(index, remaining_sum - coins[index])

        # Choice 2: skip the coin
        skip = helper(index + 1, remaining_sum)

        return take + skip

    return helper(0, total_sum)



coins = [1, 2, 3]
total_sum1 = 4
total_sum2 = 5

print(count_payment_combinations(coins, total_sum1))  # Expected: 4 ([1,1,1,1],[1,1,2],[1,3],[2,2])
print(count_payment_combinations(coins, total_sum2))  # Expected: 5 ([1,1,1,1,1],[1,1,3],[1,2,2],[2,3],[1,1,1,2])
