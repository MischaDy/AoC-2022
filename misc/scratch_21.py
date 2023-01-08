def unify_ranges(ranges):
    if len(ranges) <= 1:
        return ranges

    ranges = sorted(ranges)
    unified = []
    cur_min, cur_max = ranges[0]

    for min_, max_ in ranges[1:]:
        if min_ <= cur_max:
            cur_max = max(cur_max, max_)
            continue

        new_range = (cur_min, cur_max)
        unified.append(new_range)
        cur_min, cur_max = min_, max_

    if (cur_min, cur_max) == (min_, max_):
        new_range = (cur_min, cur_max)
        unified.append(new_range)
    return unified


# ranges = [(2, 14), (-2, 2), (16, 24), (15, 18)]
# unified_ranges = [(-2, 14), (15, 24)]
ranges = [(2, 14), (-2, 15), (17, 18), (20, 22), (15, 17)]
unified_ranges = [(-2, 18), (20, 22)]
print(ranges, unify_ranges(ranges))
assert set(unify_ranges(ranges)) == set(unified_ranges)
