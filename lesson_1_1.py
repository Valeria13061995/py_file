#Реализовать вывод информации о промежутке времени в зависимости от его
#продолжительности duration в секундах:
#a. до минуты: <s> сек;
#b. до часа: <m> мин <s> сек;
#c. до суток: <h> час <m> мин <s> сек;
#d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = 555789
print(duration, 'сек')

minute = duration // 60
second = duration % 60
print(minute, 'мин', second, 'сек')

hour = duration // 3600
minute = (duration - (hour * 3600)) // 60
print(hour, 'ч', minute, 'мин', second, 'сек')

day = hour // 24
hour = hour - (day * 24)
print(day, 'д', hour, 'ч', minute, 'мин', second, 'cек')