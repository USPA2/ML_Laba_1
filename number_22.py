# Ваша задача здесь написать функцию time_converter (именно такое название)
# она должна возвращать значения в виде строки 'hours minutes

def time_converter(str):
    hour = str / 60
    while (hour >= 24):
        hour -= 24
    new_hour = int(hour)

    while (hour > 1):
        hour -= 1
    minute = int(hour * 60.01)

    return f'{new_hour} {minute}'


assert time_converter(2782) == '22 22'
assert time_converter(4733) == '6 53'
assert time_converter(1766) == '5 26'
assert time_converter(3865) == '16 25'
assert time_converter(4628) == '5 8'
assert time_converter(4353) == '0 33'
assert time_converter(268) == '4 28'
assert time_converter(4373) == '0 53'
assert time_converter(2722) == '21 22'
assert time_converter(1531) == '1 31'


# Написать функцию min_of_three_values, принимает на вход 3 аргумента
def min_of_three_values(value_1, value_2, value_3):
    if (value_1 < value_2 < value_3) | ((value_1 < value_2 > value_3) & (value_3 > value_1)) | (value_1 == value_2 < value_3) | (value_1 == value_3 < value_2) | (value_1 < value_2 == value_3):
        return value_1
    elif (value_2 < value_1 < value_3) | (value_2 < value_3 < value_1) | (value_2 == value_1 < value_3) | (value_2 == value_3 < value_1) | (value_2 < value_1 == value_3):
        return value_2
    elif (value_3 < value_2 < value_1) | (value_3 < value_1 < value_2) | (value_3 == value_1 < value_2) | (value_3 == value_2 < value_1) | (value_3 < value_1 == value_2):
        return value_3

assert min_of_three_values(1, 2, 3) == 1
assert min_of_three_values(1, 1, 9) == 1
assert min_of_three_values(18, 7, 11) == 7
assert min_of_three_values(2, 10, 10) == 2
assert min_of_three_values(17, 14, 17) == 14
assert min_of_three_values(9, 2, 10) == 2
assert min_of_three_values(7, 4, 7) == 4
assert min_of_three_values(0, 8, 3) == 0
assert min_of_three_values(8, 10, 6) == 6
assert min_of_three_values(1, 4, 8) == 1



# Функция remove_symbol принимает два аргумента -- строку и символ, которые необходимо удалить
def remove_symbol(strok, rep):
    return strok.replace(rep, '')

assert remove_symbol('aaaaaaaa', 'a') == ''
assert remove_symbol('abababa', 'b') == 'aaaa'
assert remove_symbol('12341234', '3') == '124124'

# Функция remove_each_third_sym принимает один агрумент -- строку.
# важно -- мы считаем человеческие индексы (начиная с 1, а не 0)
# важно -- оставляем первый аргумент
# Необходимо вернуть новую строку

def remove_each_third_sym(strok):
   t = ''
   for item in range(0, len(strok)):
       if (item + 1) % 3 != 0:
           t = t + strok[item]
   return t

assert remove_each_third_sym('abcdef') == 'abde'
assert remove_each_third_sym('sdfasdfasdfsfa') == 'sdasfadffa'
assert remove_each_third_sym('123456789') == '124578'
assert remove_each_third_sym('987654321') == '986532'

# Функция find_max принимает на вход лист
# на выходе два числа -- непосредственно максимальное значение и его индекс

def find_max(values):
    max = 0
    index = 0
    for item in range(0, len(values)):
        if values[item] > max:
            max = values[item]
            index = item
    return max, index

assert find_max([1, 2, 3, 4, 5]) == (5, 4)
assert find_max([5, 4, 3, 2, 1]) == (5, 0)
assert find_max([96, 82, 72, 48, 93, 88, 79]) == (96, 0)
assert find_max([49, 75, 65, 65, 65, 18]) == (75, 1)
assert find_max([69, 16, 64, 54, 36, 70, 89, 29]) == (89, 6)
assert find_max([17, 80, 27, 36, 21, 85, 63, 27]) == (85, 5)
assert find_max([76, 27, 73, 65, 52]) == (76, 0)
assert find_max([33, 26, 69, 40, 93]) == (93, 4)
assert find_max([87, 5, 95, 52, 21, 76, 22]) == (95, 2)
assert find_max([75, 18, 89, 99, 70]) == (99, 3)

# функция append_to_list принимает два значения -- лист и значение, которое необходимо вставить в конец листа
# функция возвращает обновленный лист

def append_to_list(list, iterable):
    list.append(iterable)
    return list


assert append_to_list([1, 2], 3) == [1, 2, 3]
assert append_to_list([1, 2], None) == [1, 2, None]
assert append_to_list([1, 's'], True) == [1, 's', True]

def number_unique_elements(input_list):
    return len(set(input_list))


assert number_unique_elements([1, 2, 3]) == 3
assert number_unique_elements([1, 2, 1]) == 2
assert number_unique_elements([1, 1, 1, 1]) == 1
assert number_unique_elements([1, 2, 1, 2]) == 2