def combine_intervals(intervals):
    intervals.sort()
    return _combine_intervals(intervals)


def _combine_intervals(intervals, i=0):
    # intervals should be sorted (on first element)

    while i < len(intervals)-1:
        a,b = intervals[i]
        c,d = intervals[i+1]

        if b >= c:
            return _combine_intervals([*intervals[:i], (a,max(b,d)), *intervals[i+2:]], i)
        else:
            i += 1

    return intervals
