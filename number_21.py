import math

def difference_of_two_numbers(first, second):
    """Возвращает разницу между первым и вторым аргументом"""
    return first - second
    pass

assert difference_of_two_numbers(2, 1) == 1
assert difference_of_two_numbers(4, 1) == 3
assert difference_of_two_numbers(10, 0) == 10
assert difference_of_two_numbers(-5, -6) == 1

def condition_function(input_number):
    """
    Если входное число меньше либо равно 0, то умножить его на 2.
    В противном случае, если число больше 0, но меньше или равно 10, умножить на 3.
    Во всех прочих случаях поделить на 10.
    """
    if input_number <= 0:
        return input_number * 2
    elif input_number <= 10:
        return input_number * 3
    else:
        return input_number / 10
    pass

assert condition_function(0) == 0
assert condition_function(-1) == -2
assert condition_function(1) == 3
assert condition_function(10) == 30
assert condition_function(11) == 1.1
assert condition_function(20) == 2

def calculator(number_1, operation, number_2):
    """
    Простой оператор, способный выполнять операции +, -, *, /.
    На входе первое число, операция в виде строки и второе число.
    """
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    pass

assert calculator(1, "+", 2) == 3
assert calculator(3, "-", 1) == 2
assert calculator(4, "*", 3) == 12
assert calculator(2, "/", 2) == 1

def number_of_unique_elements(input_list):
    """
    Считает количество уникальных элементов в листе.
    """
    return len(set(input_list))
    pass


assert number_of_unique_elements([1, 2, 3]) == 3
assert number_of_unique_elements([1] * 93) == 1
assert number_of_unique_elements(list(range(1000))) == 1000

def counter(input_list):
    """
    Считает количество вхождений каждого из элементов листа.
    Возвращает словарь вида {число: количество вхождений}

    Замечание (!): встроенным в collections Counter'ом пользоваться нельзя

    Например:
    counter([1, 1, 2, 3]) вернет {1: 2, 2: 1, 3: 1}
    """
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
    pass

assert counter([1, 1, 1, 2, 3]) == {1: 3, 2: 1, 3: 1}
assert counter([1] * 1000) == {1: 1000}
assert counter([1, 3, 5] * 100) == {1: 100, 3: 100, 5: 100}

def multiply_nums(input_string):
    """
    Перемножить числа, переданные в строке, перечисленные через запятую.

    hint: можно использовать метод .split()
    """
    input_string = map(int, input_string.split(','))
    mul = 1
    for i in input_string:
        mul *= i
    return mul
    pass

assert multiply_nums("2, 3") == 6
assert multiply_nums("1, 1, 1, 1, 1, 1, 1") == 1
assert multiply_nums("345, 4576, 794, 325, 0") == 0

def custom_function(x):
    """
    Реализуйте функцию, описанную выше.
    """
    return math.sin(x) * math.cos(x)
    pass

assert round(custom_function(1), 3) == 0.455
assert round(custom_function(1.5), 3) == 0.071
assert round(custom_function(2), 3) == -0.378
assert custom_function(0) == 0

def custom_function_1(x, n):
    """
    Реализуйте функцию, описанную выше.
    """
    answer = 1
    for i in range(1, n+1):
        answer *= (pow((i + 2), x) + math.log(x)) / (pow(x, 2) + 4 * i)
    return answer
    pass

assert round(custom_function_1(2, 3), 3) == 2.707
assert round(custom_function_1(3, 2), 3) == 8.277
assert round(custom_function_1(3, 3), 3) == 49.7


