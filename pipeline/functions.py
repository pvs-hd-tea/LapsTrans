def increment(inp):
    # list-of-int -> list-of-int #
    return [each + 1 for each in inp]


def decrement(inp):
    # list-of-int -> list-of-int #
    return [each - 1 for each in inp]


def multiply_by_five(inp):
    # list-of-int -> list-of-int #
    return [each * 5 for each in inp]


def delete_last(inp):
    # list-of-int -> list-of-int #
    inp.pop()
    return inp


def sum_list(inp):
    # list-of-int -> int #
    accu = 0
    for each in inp:
        accu += each
    return accu


def max_val(inp):
    # list-of-int -> int #
    return max(inp)


def lenght(inp):
    # list-of-int -> int #
    return len(inp)


def average(inp):
    # list-of-int -> int #
    return sum_list(inp) // len(inp)


def add_zero_to_end(inp):
    # list-of-int -> list-of-int #
    inp.append(0)
    return inp

def count_ones(inp):
    # list-of-int -> int #
    accu = 0
    for each in inp:
        if each == 1:
            accu += 1
    return accu


def reverse_list(inp):
    # list-of-int -> list-of-int #
    return inp[::-1]


def mirror(inp):
    # list-of-int -> list-of-int #
    return inp + inp[::-1]


def exchange_fours_to_ones(inp):
    # list-of-int -> list-of-int #
    for i in range(len(inp)):
        if inp[i] == 4:
            inp[i] = 1
    return inp


def delete_even_indx(inp):
    # list-of-int -> list-of-int #
    del inp[1::2]
    return inp


def copy_list(inp):
    # list-of-int -> list-of-int #
    return inp + inp

def change_max_val_to_zero(inp):
    # list-of-int -> list-of-int #
    for i in range(len(inp)):
        if inp[i] == max(inp):
            inp[i] = 0
    return inp

def add_zero_if_ends_with_6(inp):
    # list-of-int -> list-of-int #
    if inp[len(inp) - 1] == 6:
        inp.append(0)
    return inp


def if_contains_3_do_reverse(inp):
    # list-of-int -> list-of-int #
    if 3 in inp:
        return inp[::-1]
    else:
        return inp

