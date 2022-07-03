def decrement(inp):
    # list-of-int -> list-of-int #
    return [each - 1 for each in inp]


def sum(inp):
    # list-of-int -> int #
    accu = 0
    for each in inp:
        accu += each
    return accu
