def increment(inp):
    return [each + 1 for each in inp]


def decrement(inp):
    return [each - 1 for each in inp]


def delete_last(inp):
    return inp[:-1]


def delete_first(inp):
    return inp[1:]


def take_first(inp):
    return inp[0]


def take_last(inp):
    return inp[-1]


def take_first_and_last(inp):
    return [inp[0]] + [inp[-1]]


def minimum(inp):
    return min(inp)


def maximum(inp):
    return max(inp)


def floor_list(inp):
    return [min(inp) for _ in inp]


def ceil_list(inp):
    return [max(inp) for _ in inp]


def ceil_list(inp):
    return [max(inp) for _ in inp]


def odd_indexes(inp):
    return inp[1::2]


def even_indexes(inp):
    return inp[0::2]


def even(inp):
    return inp % 2 == 0


def odd(inp):
    return inp % 2 != 0


def multiply_by_2(inp):
    return [each * 2 for each in inp]


def multiply_by_4(inp):
    return [each * 4 for each in inp]


def multiply_by_5(inp):
    return [each * 5 for each in inp]


def sum_list(inp):
    return sum(inp)


def lenght(inp):
    return len(inp)


def average(inp):
    return sum_list(inp) // len(inp)


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


def replace_all_with_sum(inp):
    s = sum(inp)
    return [s for _ in inp]


def zero(inp):
    return [0 for _ in inp]


def flat_zero(inp):
    return 0


def flat_1(inp):
    return 1


def half_even(inp):
    return [x/2 if x % 2 == 0 else x for x in inp]


def increment_odd(inp):
    return [x+1 if x % 2 != 0 else x for x in inp]


def replace_4_1(inp):
    return [1 if x == 4 else x for x in inp]


def replace_5_1(inp):
    return [1 if x == 5 else x for x in inp]


def replace_2_5(inp):
    return [5 if x == 2 else x for x in inp]


def replace_1_9(inp):
    return [9 if x == 1 else x for x in inp]


def first_half(inp):
    return inp[:len(inp)//2+1]


def second_half(inp):
    return inp[len(inp)//2:]


def s(inp):
    return sorted(inp)


def rs(inp):
    return sorted(inp, reverse=True)


def duplicate(inp):
    return inp + inp


def change_max_val_to_zero(inp):
    m = max(inp)
    return [0 if x == m else x for x in inp]


def average_all(inp):
    a = sum(inp)//len(inp)
    return [a for _ in inp]


def reverse_if_contains_0(inp):
    if 0 in inp:
        return inp[::-1]
    else:
        return inp


def reverse_if_contains_3(inp):
    if 3 in inp:
        return inp[::-1]
    else:
        return inp


def reverse_if_contains_5(inp):
    if 5 in inp:
        return inp[::-1]
    else:
        return inp


def add_zero_if_ends_with_6(inp):
    if inp[-1] == 6:
        return inp + [0]
    return inp


def increment_if_contains_0(inp):
    if 0 in inp:
        return [x+1 for x in inp]
    return inp


def decrement_if_contains_0(inp):
    if 0 in inp:
        return [x-1 for x in inp]
    return inp


def double_if_contains_0(inp):
    if 0 in inp:
        return [x*2 for x in inp]
    return inp


def increment_if_contains_3(inp):
    if 3 in inp:
        return [x+1 for x in inp]
    return inp


def decrement_if_contains_3(inp):
    if 3 in inp:
        return [x-1 for x in inp]
    return inp


def double_if_contains_3(inp):
    if 3 in inp:
        return [x*2 for x in inp]
    return inp


def increment_if_contains_5(inp):
    if 5 in inp:
        return [x+1 for x in inp]
    return inp


def decrement_if_contains_5(inp):
    if 5 in inp:
        return [x-1 for x in inp]
    return inp


def double_if_contains_5(inp):
    if 5 in inp:
        return [x*2 for x in inp]
    return inp


def contains_0(inp):
    return 0 in inp


def contains_2(inp):
    return 2 in inp


def contains_3(inp):
    return 3 in inp


def not_contains_0(inp):
    return 0 not in inp


def not_contains_5(inp):
    return 5 not in inp


def n(b):
    return not b


def r(inp):
    return list(range(inp))


def nr(inp):
    return [-i for i in range(inp)]


def fibb(inp):
    r = [1]
    for i in range(1, inp+1):
        r.append(i + r[i-1])
    return r
