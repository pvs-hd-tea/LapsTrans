def reverse(inp):
    # list-of-int -> list-of-int #
    return list(reversed(inp))

def mirror(inp):
    # list-of-int -> list-of-int #
    return inp + list(reversed(inp))

def decrement(inp):
    # list-of-int -> list-of-int #
    return [each - 1 for each in inp]


def sum(inp):
    # list-of-int -> int #
    accu = 0
    for each in inp:
        accu += each
    return accu
