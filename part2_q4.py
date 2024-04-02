def max_activities(activities):
    activities.sort(key=lambda x: x[1])
    max_count = 1
    prev_end = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= prev_end:
            max_count += 1
            prev_end = activities[i][1]

    return max_count

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
print(max_activities(activities))
