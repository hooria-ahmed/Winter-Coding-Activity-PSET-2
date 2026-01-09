import math

def calculate_minimum_speed(piles, k):
    speed = 1
    max_pile = max(piles)

    while speed <= max_pile:
        hours = sum(math.ceil(pile / speed) for pile in piles)
        if hours <= k:
            return speed
        speed += 1

    return max_pile  # fallback, if speed = max_pile is needed



piles1 = [3, 6, 7, 11]
k1 = 8

piles2 = [30, 11, 23, 4, 20]
k2 = 5

print(calculate_minimum_speed(piles1, k1))  # Expected: 4
print(calculate_minimum_speed(piles2, k2))  # Expected: 30
