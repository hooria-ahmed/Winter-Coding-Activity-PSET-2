def can_balance_scales(arr):
    total_sum = sum(arr)

    # Step 1: Parity check
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    # Step 2: DP array
    dp = [False] * (target + 1)
    dp[0] = True

    # Step 3: Fill DP
    for weight in arr:
        for s in range(target, weight - 1, -1):
            dp[s] = dp[s] or dp[s - weight]

    return dp[target]


arr1 = [1, 2, 3, 4]
arr2 = [1, 1, 3]
arr3 = [2, 2, 2, 2]

print(can_balance_scales(arr1))  # Expected: True 
print(can_balance_scales(arr2))  # Expected: False 
print(can_balance_scales(arr3))  # Expected: True 
