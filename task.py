"""
Дано: строка содержащая только скобки 3х видов и открывающиеся и закрывающися.

“[{}({})]” - валидно
“[[” - не валидно
“[{]}” - не валидно

Написать функцию определения валидности строки: чтобы все скобки имели
закрывающую пару и корректную вложенность.
"""
from re import sub


class Statuses:
    VALID = 'valid'
    NON_VALID = 'non valid'


def check_valid_str(string: str) -> str:
    l = len(string)
    if l and l % 2:
        return Statuses.NON_VALID
    while l:
        string = sub(r'(\(\))|(\{\})|(\[\])', '', string)
        new_l = len(string)

        if l == new_l:
            return Statuses.NON_VALID

        l = new_l

    return Statuses.VALID


assert check_valid_str('[{}({})]') == Statuses.VALID
assert check_valid_str('[{}({})') == Statuses.NON_VALID
assert check_valid_str('[[]]') == Statuses.VALID
assert check_valid_str('[[') == Statuses.NON_VALID
assert check_valid_str('[{]}') == Statuses.NON_VALID
