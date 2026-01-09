def find_longest_mirror_length(s: str) -> int:
    def helper(i, j):
        # Base cases
        if i > j:
            return 0
        if i == j:
            return 1

        # Characters match
        if s[i] == s[j]:
            return 2 + helper(i + 1, j - 1)

        # Characters do not match
        return max(helper(i + 1, j), helper(i, j - 1))

    return helper(0, len(s) - 1)




s1 = "racecar"
s2 = "abcde"
s3 = "aabccbaa"

print(find_longest_mirror_length(s1))  # Expected: 7
print(find_longest_mirror_length(s2))  # Expected: 1

