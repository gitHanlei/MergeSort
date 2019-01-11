# coding utf-8
import math


def merge(list_one, list_two):
    """

    :param list_one: sorted list
    :param list_two: sorted list
    :return: sorted list
    """
    ret_list = []
    length_one = len(list_one)
    length_two = len(list_two)

    i, j = 0, 0
    while True:

        if i >= length_one:
            ret_list.extend(list_two[j:])
            break

        if j >= length_two:
            ret_list.extend(list_one[i:])
            break

        if list_one[i] < list_two[j]:
            ret_list.append(list_one[i])
            i += 1
            continue

        if list_one[i] >= list_two[j]:
            ret_list.append(list_two[j])
            j += 1
            continue
    return ret_list


def merge_sort(source_list):
    l = len(source_list)
    if l < 2:
        return source_list
    num = math.ceil(l / 2)
    left = merge_sort(source_list[:num])
    right = merge_sort(source_list[num:])
    return merge(left, right)


if __name__ == "__main__":
    a = [3, 100, 6, 19, 10, 80, 4, 90, 3, 100, 6, 19, 10, 80, 4, 90, 3, 100, 6, 19, 10, 80, 4, 90, 3, 100, 6, 19, 10,
         80, 4, 90, 1, 10000]
    print(merge_sort(a))
