def find_longest_mirror_length(s: str) -> int:
    n = len(s)

    # dp[i][j] = LPS length from i to j
    dp = [[0] * n for _ in range(n)]

    # Single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill table bottom-up
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]




s1 = "racecar"
s2 = "abcde"
s3 = "aabccbaa"

print(find_longest_mirror_length(s1))  # Expected: 7
print(find_longest_mirror_length(s2))  # Expected: 1

