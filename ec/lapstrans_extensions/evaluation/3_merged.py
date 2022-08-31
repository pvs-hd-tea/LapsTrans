def delete_first_append_max_zero_min(inp):
    q = inp[1:]
    q = q + [max(q)]
    q = [0 if x == min(q) else x for x in q]
    return q


def range_max_if_first_is_min(inp):
    if inp[0] == min(inp):
        return list(range(max(inp)))
    return inp


def floor_if_contains_2_else_ceil(inp):
    if 2 in inp:
        return [min(inp) for _ in inp]
    else:
        return [max(inp) for _ in inp]


def reverse_negative_range(inp):
    return [-i for i in range(inp-1, -1, -1)]
