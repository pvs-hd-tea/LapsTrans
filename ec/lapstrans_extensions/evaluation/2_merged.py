def replace_max_with_sum(inp):
    s = sum(inp)
    return [s if x == max(inp) else x for x in inp]


def if_contains_2_floor(inp):
    if 2 in inp:
        return [min(inp) for _ in inp]
    return inp


def n_ns(inp):
    return [inp for _ in range(inp)]


def if_min_is_0(inp):
    return min(inp) == 0
