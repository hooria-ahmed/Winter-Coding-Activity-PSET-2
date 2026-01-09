def count_ways_to_summit(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Test Case 1
print(count_ways_to_summit(5))  # Expected: 8 (1+2+3+5th term in Fibonacci-like series)

# Test Case 2
print(count_ways_to_summit(10))  # Expected: 89
