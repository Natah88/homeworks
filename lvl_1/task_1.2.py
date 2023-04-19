# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

from random import randint
i, time = 0, 0
while i < 4:
    x = my_favorite_songs[randint(0, len(my_favorite_songs)-1)]
    time += float(x[1])
    i += 1
#print(f'Три песни звучат {time} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

from random import randrange
i, time = 0, 0
while i < 4:
    d = list(my_favorite_songs_dict.values())
    time += d[randrange(len(d))]
    i += 1
print(f'Три песни звучат {time} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random


import random
songs = list(my_favorite_songs_dict.keys())
song = random.choice(songs)
print(f'Случайная песня из словаря {song}')

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

from datetime import datetime

time_song = str(my_favorite_songs_dict.values())
n = time_song[0]
#time_in_minutes = datetime.strptime(time_song)

print((time_song))
