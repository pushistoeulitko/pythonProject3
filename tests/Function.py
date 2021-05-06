import re
from tests import DATA
from collections import Counter


def print_value(func):
    def wrapper(*args):
        func(*args)
        last_ten = ''.join(str(args[0][len(args[0]) - 10:]))
        first_ten = ''.join(str(args[0][:10]))
        print('Первые 10 значений:\n' + first_ten + '\nПоследние 10 значений:\n' + last_ten)
        return args

    return wrapper


@print_value
def loading(collect, sort_file):
    with open(sort_file, "r") as file:
        for line in file:
            simple_key = re.findall(r'(\b\w+\b)', line)[0]
            simple_value = re.findall(r'\b\d+\b', line)[0]
            obj = DATA.Data(simple_key, simple_value, '')
            collect.append(obj)
        return collect


@print_value
def adding_an_additional_parameter(collect):
    num_list = []
    for i in range(len(collect)):
        num = collect[i].simple_value
        num_list.append(num)
    dict_frequency = Counter(num_list)
    for y in range(len(collect)):
        date_y = collect[y]
        val = date_y.simple_value
        simple_count = dict_frequency.get(val)
        date_y.simple_count = simple_count
    return collect


@print_value
def sorting(collect, sorting_order):
    if sorting_order.lower() == 'asc':
        sort = True
    else:
        sort = False
    collect.sort(key=lambda data: int(data.simple_count), reverse=sort)
    return collect


@print_value
def saving_to_a_file(collect, output_file):
    with open(output_file, "w") as file:
        for y in range(len(collect)):
            line = str(collect[y]) + '\n'
            file.write(line)


def load_sort_add_counter_and_save_in_file(sort_file, sorting_order, output_file):
    collect = []
    loading(collect, sort_file)
    adding_an_additional_parameter(collect)
    sorting(collect, sorting_order)
    saving_to_a_file(collect, output_file)


load_sort_add_counter_and_save_in_file("simple.dat", "Asc", "simple3.dat")
