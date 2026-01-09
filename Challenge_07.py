import math

def calculate_minimum_speed(piles, k):
    left = 1
    right = max(piles)

    def hours_needed(speed):
        return sum(math.ceil(pile / speed) for pile in piles)

    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= k:
            # Try a smaller speed
            right = mid
        else:
            # Speed too slow, increase it
            left = mid + 1

    return left




piles1 = [3, 6, 7, 11]
k1 = 8

piles2 = [30, 11, 23, 4, 20]
k2 = 5

print(calculate_minimum_speed(piles1, k1))  # Expected: 4
print(calculate_minimum_speed(piles2, k2))  # Expected: 30
