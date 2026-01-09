def min_cancelled_bookings(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    removals = 0
    end = float('-inf')

    for start, finish in intervals:
        if start >= end:
            # Accept meeting
            end = finish
        else:
            # Overlap → remove meeting
            removals += 1

    return removals




intervals1 = [(1, 3), (2, 4), (3, 5)]
intervals2 = [(1, 2), (2, 3), (3, 4)]
intervals3 = [(1, 10), (2, 3), (3, 4)]

print(min_cancelled_bookings(intervals1))  # Expected: 1
print(min_cancelled_bookings(intervals2))  # Expected: 0
print(min_cancelled_bookings(intervals3))  # Expected: 1
