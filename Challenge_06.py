def maximize_freelance_profit(deadlines, profits):
    def find(slot):
        # Path compression
        if parent[slot] != slot:
            parent[slot] = find(parent[slot])
        return parent[slot]

    jobs = list(zip(deadlines, profits))
    # Sort jobs by profit descending
    jobs.sort(key=lambda x: x[1], reverse=True)

    max_deadline = max(deadlines)
    parent = [i for i in range(max_deadline + 1)]  # DSU parent array

    total_jobs = 0
    total_profit = 0

    for deadline, profit in jobs:
        available_slot = find(deadline)
        if available_slot > 0:
            # Assign job to this slot
            total_jobs += 1
            total_profit += profit
            # Mark this slot as filled: next available is slot-1
            parent[available_slot] = find(available_slot - 1)

    return [total_jobs, total_profit]


deadlines = [2, 1, 2, 1, 3]
profits = [100, 19, 27, 25, 15]

print(maximize_freelance_profit(deadlines, profits))  # Expected: [3, 142] (3 jobs, total profit 142)
