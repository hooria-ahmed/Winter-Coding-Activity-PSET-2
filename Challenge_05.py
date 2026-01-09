def min_cancelled_bookings(intervals):
    def is_overlap(a, b):
        return a[1] > b[0] and b[1] > a[0]

    n = len(intervals)
    if n <= 1:
        return 0

    # Recursive helper
    def helper(index, accepted):
        if index == n:
            return 0

        # Option 1: skip current meeting
        skip = 1 + helper(index + 1, accepted)

        # Option 2: accept current meeting if no overlap with accepted meetings
        can_accept = True
        for a in accepted:
            if is_overlap(a, intervals[index]):
                can_accept = False
                break

        take = 0
        if can_accept:
            take = helper(index + 1, accepted + [intervals[index]])

        return min(skip, take)

    return helper(0, [])




intervals1 = [(1, 3), (2, 4), (3, 5)]
intervals2 = [(1, 2), (2, 3), (3, 4)]
intervals3 = [(1, 10), (2, 3), (3, 4)]

print(min_cancelled_bookings(intervals1))  # Expected: 1
print(min_cancelled_bookings(intervals2))  # Expected: 0
print(min_cancelled_bookings(intervals3))  # Expected: 1
