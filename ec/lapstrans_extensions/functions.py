def increment(inp):
    return [each + 1 for each in inp]


def decrement(inp):
    return [each - 1 for each in inp]


def multiply_by_five(inp):
    return [each * 5 for each in inp]


def delete_last(inp):
    inp.pop()
    return inp


def sum_list(inp):
    accu = 0
    for each in inp:
        accu += each
    return accu


def max_val(inp):
    return max(inp)


def lenght(inp):
    return len(inp)


def average(inp):
    return sum_list(inp) // len(inp)


def add_zero_to_end(inp):
    inp.append(0)
    return inp


def count_ones(inp):
    accu = 0
    for each in inp:
        if each == 1:
            accu += 1
    return accu


def reverse_list(inp):
    return inp[::-1]


def mirror(inp):
    return inp + inp[::-1]


def exchange_fours_to_ones(inp):
    for i in range(len(inp)):
        if inp[i] == 4:
            inp[i] = 1
    return inp


def delete_even_indx(inp):
    del inp[1::2]
    return inp


def copy_list(inp):
    return inp + inp


def change_max_val_to_zero(inp):
    for i in range(len(inp)):
        if inp[i] == max(inp):
            inp[i] = 0
    return inp


def add_zero_if_ends_with_6(inp):
    if inp[len(inp) - 1] == 6:
        inp.append(0)
    return inp


def if_contains_3_do_reverse(inp):
    if 3 in inp:
        return inp[::-1]
    else:
        return inp
