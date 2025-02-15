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
# pprint(list_number)

# 3 пункт задания - перепаковка full_dict с сохранением id 
full_list = [{"id": film_id, **film} for film_id, film in full_dict.items()]
# pprint(full_list)

# 4 пункт задания - с помощью filter создаю список содержащий исходные id и ключи словаря full_dict, id должны быть те, которые есть в списке list_number
list_id = list(filter(lambda x: x['id'] in list_number, full_list))
# pprint(list_id)

# 5 пункт задания - Создайю множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.
set_director = {film['director'] for film in full_list}
# pprint(set_director)

# 6 пункт задания - С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку.
copy_dict = {key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()}
# pprint(copy_dict)

# 7 пункт задания - Используйте `filter`, чтобы получить словари, содержащий только те фильмы, которые начинаются на букву `Ч`.
filter_dict = list(filter(lambda x: x['title'].startswith('Ч') if x['title'] is not None else False, full_list))
# pprint(filter_dict)

# 8 пункт задания - Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку. 
# Сортировка по названию фильма (по алффавиту)
def film_sort(film):    
    title = film['title']
    title = title if title else 'без названия'
    return title

full_list.sort(key=film_sort)
pprint(full_list)