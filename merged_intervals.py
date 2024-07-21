def merge_intervals(intervals: list) -> list:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    return merged


interval_list = [
    (1, 3),
    (2, 4),
    (5, 7),
    (6, 8),
    (10, 12),
    (11, 15)
]

merged_intervals = merge_intervals(interval_list)

print(merged_intervals)