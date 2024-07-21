from utils import *


def calc_unions(base2, sublist, end):
    res = []
    for item in sublist:
        res.append(sieve(item, base2, end))
    final_list = []
    for sublist in res:
        for item in sublist:
            final_list.append(item)
    final_list.sort()
    return final_list


def sieve_matrix(base1, base2, list_of_lists):
    res = []
    end = base1 * base2
    for i, sublist in enumerate(list_of_lists):
        unions = calc_unions(base2, sublist, end)
        temp = sieve(i, base1, end)
        res.append(list(set(unions).intersection(temp)))
    final_list = []
    for sublist in res:
        for item in sublist:
            final_list.append(item)
    final_list.sort()

    return final_list


print(sieve_matrix(7, 5,
                   [[0, 1, 2, 4],
                    [2, 4],
                    [1, 2, 4],
                    [1, 2, 4],
                    [1, 4],
                    [0, 1, 2, 4],
                    [2]]
                   ))
