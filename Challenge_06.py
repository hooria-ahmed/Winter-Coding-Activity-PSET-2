def maximize_freelance_profit(deadlines, profits):
    jobs = list(zip(deadlines, profits))
    # Sort by profit descending
    jobs.sort(key=lambda x: x[1], reverse=True)

    max_deadline = max(deadlines)
    slots = [False] * (max_deadline + 1)  # Hour slots: 1..max_deadline

    total_jobs = 0
    total_profit = 0

    for deadline, profit in jobs:
        # Try to schedule in the latest available slot <= deadline
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                total_jobs += 1
                total_profit += profit
                break  # Job scheduled, move to next

    return [total_jobs, total_profit]



deadlines = [2, 1, 2, 1, 3]
profits = [100, 19, 27, 25, 15]

print(maximize_freelance_profit(deadlines, profits))  # Expected: [3, 142] (3 jobs, total profit 142)
