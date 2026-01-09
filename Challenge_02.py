def can_balance_scales(arr):
    total_sum = sum(arr)

    # If total sum is odd, we cannot split it evenly
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    def dfs(index, current_sum):
        # Success case
        if current_sum == target:
            return True

        # Failure cases
        if index == len(arr) or current_sum > target:
            return False

        # Choice 1: include current stone
        if dfs(index + 1, current_sum + arr[index]):
            return True

        # Choice 2: exclude current stone
        return dfs(index + 1, current_sum)

    return dfs(0, 0)



arr1 = [1, 2, 3, 4]
arr2 = [1, 1, 3]
arr3 = [2, 2, 2, 2]

print(can_balance_scales(arr1))  # Expected: True 
print(can_balance_scales(arr2))  # Expected: False 
print(can_balance_scales(arr3))  # Expected: True 
