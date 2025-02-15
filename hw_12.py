"""
hw_12: Работа с дата-сетом Marvel. 
Используемые функции и инструменты:
- `map()`
- `filter()`
- `lambda`
- `set comprehension`
- `dict comprehension`
- `pprint`

Для корректной работы с кодом нужно:
- from marvel import full_dict
- from pprint import pprint
"""

from marvel import full_dict
from pprint import pprint

# 1 пункт задания - запрос у пользователя списка цифр через пробел 
user_input = input("Введите цифры через пробел: ")

# 2 пункт задания - превратил введёные цифры в список, если не цифры, то None
list_number = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

# 3 пункт задания - перепаковка full_dict с сохранением id 
full_list = [{"id": film_id, **film} for film_id, film in full_dict.items()]

# 4 пункт задания - с помощью filter создаю список содержащий исходные id и ключи словаря full_dict, id должны быть те, которые есть в списке list_number
list_id = list(filter(lambda x: x['id'] in list_number, full_list))

# 5 пункт задания - Создайю множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.
set_director = {film['director'] for film in full_list}

# 6 пункт задания - С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку.
copy_dict = {key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()}

# 7 пункт задания - Используйте `filter`, чтобы получить словари, содержащий только те фильмы, которые начинаются на букву `Ч`.
filter_dict = list(filter(lambda x: x['title'].startswith('Ч') if x['title'] is not None else False, full_list))

# 8 пункт задания - Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку. 
# Сортировка по названию фильма (по алффавиту)
def film_sort(film):    
    title = film['title']
    title = title if title else 'без названия'
    return title

full_list.sort(key=film_sort)

# 9 пункт задания - Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.
# Сортировка по году выпуска и названию фильма (сначала по году, потом по алфавиту)
def film_sort_two(film):    
    title = film['title']
    year = film['year']
    title = title if title else 'без названия'
    year = year if isinstance(year, int) else 0
    return year, title

full_list.sort(key=film_sort_two)

# 10 пункт задания - Напишите однострочник, который отфильтрует и отсортирует `full_dict` с использованием `filter` и `sorted`.
# Фильтрация по году , а потом сортировка 
sorted_2023 = list(sorted(filter(lambda film: film['year'] == 2023, full_list), key=lambda film: film['title']))


# 11 пункт 
# Вывод всех pprint с подписью о том, что выводится 
print("\nЗадание 1: Список введённых пользователем чисел:")
pprint(user_input, width=100, compact=True)

print("\nЗадание 2: Список с id из user_input:")
pprint(list_number, width=100, compact=True)

print("\nЗадание 3: Перепаковка full_dict с сохранением id:")
pprint(full_list, width=100, compact=True)

print("\nЗадание 4: Список с id из user_input:")
pprint(list_id, width=100, compact=True)

print("\nЗадание 5: Множество с уникальными значениями ключа director:")
pprint(set_director, width=100, compact=True)

print("\nЗадание 6: Копия словаря full_dict, где значения ключа 'year' преобразованы в строку:")
pprint(copy_dict, width=100, compact=True)

print("\nЗадание 7: Фильмы, начинающиеся на букву 'Ч':")
pprint(filter_dict, width=100, compact=True)

print("\nЗадание 8: Сортировка по названию фильма:")
pprint(full_list, width=100, compact=True)

print("\nЗадание 9: Сортировка по году выпуска и названию фильма:")
pprint(full_list, width=100, compact=True)

print("\nЗадание 10: Отфильтрованный и отсортированный список:")
pprint(sorted_2023, width=100, compact=True)