import re
from tests import DATA
from collections import Counter

collect_date = []
collect_with_add_element = []
sort_collect = []


def print_value(func):
    def wrapper(collect):
        func()
        last_ten = ''.join(str(collect[len(collect) - 10:]))
        first_ten = ''.join(str(collect[:10]))
        print('Первые 10 значений:\n' + first_ten + '\nПосленидие 10 значений:\n' + last_ten)

    return wrapper


@print_value
def loading():
    with open("simple.dat", "r", encoding="utf-8") as file:
        for line in file:
            simple_key = re.findall(r'(\b\w+\b)', line)[0]
            simple_value = re.findall(r'\b\d+\b', line)[0]
            obj = DATA.Data(simple_key, simple_value)
            collect_date.append(obj)
        return collect_date


@print_value
def adding_an_additional_parameter():
    num_list = []
    for i in range(len(collect_date) - 1):
        num = collect_date[i].simple_value
        num_list.append(num)
    dict_frequency = Counter(num_list)
    for y in range(len(collect_date) - 1):
        val = collect_date[y].simple_value
        key = collect_date[y].simple_key
        simple_count = dict_frequency.get(val)
        obj2 = DATA.Data(key, val, simple_count)
        collect_with_add_element.append(obj2)
    return collect_with_add_element


@print_value
def sorting(sort=bool):
    if sort == bool:
        sort_type = True
    if sort != bool:
        sort_type = False
    sort_items = sorted(collect_with_add_element, key=lambda data: int(data.simple_count), reverse=sort_type)
    sort_collect.extend(sort_items)
    return sort_collect


@print_value
def saving_to_a_file():
    with open("simple2.dat", "w", encoding="utf-8") as file:
        for y in range(len(sort_collect) - 1):
            line = str(sort_collect[y]) + '\n'
            file.write(line)


def load_sort_add_counter_and_save_in_file():
    loading(collect_date)
    adding_an_additional_parameter(collect_with_add_element)
    sorting(sort_collect)
    saving_to_a_file(sort_collect)


load_sort_add_counter_and_save_in_file()
