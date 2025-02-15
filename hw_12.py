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