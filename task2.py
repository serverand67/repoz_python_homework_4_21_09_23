# Задача 2.
# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление. 
# пример:
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> 
# {True: "rev", "YES": 'acc', 4: "stroka"} 


def reverse_key_value(**kwargs):
    return {value: key for key, value in kwargs.items()}


result = reverse_key_value(rev=True, acc="YES", stroka=4)
print(result)