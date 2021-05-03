import re
from tests import DATA
from collections import Counter

collect_date = []


def print_value(func):
    def wrapper():
        func()
        last_ten = ''.join(str(collect_date[len(collect_date) - 10:]))
        first_ten = ''.join(str(collect_date[:10]))
        print('Первые 10 значений:\n' + first_ten + '\nПоследние 10 значений:\n' + last_ten)
    return wrapper


@print_value
def loading():
    with open("simple.dat", "r") as file:
        for line in file:
            simple_key = re.findall(r'(\b\w+\b)', line)[0]
            simple_value = re.findall(r'\b\d+\b', line)[0]
            obj = DATA.Data(simple_key, simple_value, '')
            collect_date.append(obj)
        return collect_date


@print_value
def adding_an_additional_parameter():
    num_list = []
    for i in range(len(collect_date)):
        num = collect_date[i].simple_value
        num_list.append(num)
    dict_frequency = Counter(num_list)
    for y in range(len(collect_date)):
        date_y = collect_date[y]
        val = date_y.simple_value
        simple_count = dict_frequency.get(val)
        date_y.simple_count = simple_count


@print_value
def sorting(sort_type=False):
    if sort_type != bool:
        sort_type = True
    collect_date.sort(key=lambda data: int(data.simple_count), reverse=sort_type)


@print_value
def saving_to_a_file():
    with open("simple2.dat", "w") as file:
        for y in range(len(collect_date)):
            line = str(collect_date[y]) + '\n'
            file.write(line)


def load_sort_add_counter_and_save_in_file():
    loading()
    adding_an_additional_parameter()
    sorting()
    saving_to_a_file()


load_sort_add_counter_and_save_in_file()
