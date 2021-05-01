import re
from tests import DATA
from collections import Counter


def print_value(func, collect):
    func()
    last_ten = collect[len(collect) - 10:]
    first_ten = collect[:10]
    print(f'Первые 10 значений: {first_ten}\nПосленидие 10 значений: {last_ten}')


collect_date = []


# @print_value
def loading():
    print('e')
    with open("simple.dat", "r", encoding="utf-8") as file:
        for line in file:
            # string = line.split(', ')
            # simple_key = string[:-1]
            # simple_value = string[-1:]
            simple_key = re.findall(r'(\b\w+\b)', line)[0]  # [^,]
            simple_value = re.findall(r'\b\d+\b', line)[0]
            obj = DATA.Data(simple_key, simple_value)
            collect_date.append(obj)
        return collect_date


loading()


sort_collect = []

# @print_value(sort_collect)
def sorting(sort=bool):
    if sort == bool:
        sort_type = False
    if sort != bool:
        sort_type = True

    sort_items = sorted(collect_date, key=lambda data: int(data.simple_value), reverse=sort_type)
    sort_collect.extend(sort_items)
    return sort_collect


sorting()

collect_with_add_element=[]

# @print_value
def adding_an_additional_parameter():
    num_list=[]
    for i in range(len(sort_collect) - 1):
        num = sort_collect[i].simple_value
        num_list.append(num)
    a=Counter(num_list)
    for y in range(len(sort_collect) - 1):
        b=sort_collect[y].simple_value
        c=sort_collect[y].simple_key
        simple_count=a.get(b)
        obj2 = DATA.Data(c, b, simple_count)
        collect_with_add_element.append(obj2)
    return collect_with_add_element


adding_an_additional_parameter()


# @print_value
def saving_to_a_file():
    with open("simple2.dat", "w", encoding="utf-8") as file:
        for line in file:



