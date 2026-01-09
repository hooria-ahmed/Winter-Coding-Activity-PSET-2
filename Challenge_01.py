def count_ways_to_summit(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways_to_summit(n - 1) + count_ways_to_summit(n - 2)


# Test Case 1
print(count_ways_to_summit(5))  # Expected: 8 (1+2+3+5th term in Fibonacci-like series)

# Test Case 2
print(count_ways_to_summit(10))  # Expected: 89
