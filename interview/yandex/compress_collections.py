"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку,
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
"""


def collapse_interval(interval_in, interval_out) -> str:
    """Схлопывание инвервала."""
    if not interval_out or interval_in == interval_out:
        return f"{interval_in}"
    return f"{interval_in}-{interval_out}"


def compress(value: list) -> str:
    """Свертка списка в диапазоны."""
    if not len(value):
        return ""
    if len(value) == 1:
        return f"{value[0]}"

    value.sort()
    result = []
    index = 1
    interval_in = value[0]
    interval_out = None

    while(True):
        if index == len(value):
            break
        if value[index - 1] == value[index] - 1:
            interval_out = value[index]
        else:
            result.append(collapse_interval(interval_in, interval_out))
            interval_in = value[index]
            interval_out = None
        index += 1
    result.append(collapse_interval(interval_in, interval_out))
    return ",".join(result)


assert compress([]) == ""
assert compress([1]) == "1"
assert compress([1, 4, 5, 2, 3, 9, 8, 11, 0]) == "0-5,8-9,11"
assert compress([1, 4, 3, 2]) == "1-4"
assert compress([1, 4]) == "1,4"
