from random import randint


num_list = [randint(1, 99) for _ in range(100)]

print(num_list)


def merge_lists(list_one: list, list_two: list) -> list[int]:
    '''слияние двух отсортированных массивов'''

    res_list = []

    i = 0
    j = 0

    while i < len(list_one) and j < len(list_two):
        if list_one[i] < list_two[j]:
            # minimum = list_one.pop(i)
            minimum = list_one[i]
            res_list.append(minimum)
            i += 1
        else:
            # minimum = list_two.pop(j)
            minimum = list_two[j]
            res_list.append(minimum)
            j += 1

    while i < len(list_one):
        res_list.append(list_one[i])
        i += 1
    while j < len(list_two):
        res_list.append(list_two[j])
        j += 1

    return res_list


def list_division(big_list: list) -> tuple[list[int], list[int]]:
    '''деление массива на два'''
    list_one = big_list[:int(len(big_list)/2)]
    list_two = big_list[int(len(big_list)/2):]
    return list_one, list_two


def merge_sorting(array_to_sort: list) -> list[int]:
    '''основная функция сортировки'''
    if len(array_to_sort) < 2:
        return array_to_sort
    else:
        return merge_lists(merge_sorting(list_division(array_to_sort)[0]),
                           merge_sorting(list_division(array_to_sort)[1]))


print(merge_sorting(num_list))
