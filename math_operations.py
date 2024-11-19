
#Дополнение
answer = 10 + 20
print('ответ:')
print(answer)
print('следующее задание')
#Вычитание

difference = 20 - 15
print('ответ:')
print(difference)
print('следующее задание')
#Умножение
product = 30*10
print('ответ:')
print(product)
print('следующее задание')
#Подразделение
quotient = 30/10
print('ответ:')
print(quotient)
print('следующее задание')
#работа с делением
seconds = 1042

display_minutes = seconds // 60 
print('ответ:')
print (display_minutes)
#17 выходные данные
display_seconds = seconds % 60
print('ответ:')
print(display_seconds)
print('следующее задание')
#выходные данные 22(деление с остатком)


#Порядок операций
result_1 = 1000 + 50 * 2 
print('ответ:')
print(result_1)

result_2 = 1000 + (50*2)
print('ответ:')
print(result_2)
#Ответ одинаковый


print("След задание")



first_planet = 122123123
second_planet = 99999999

distance_km = second_planet - first_planet
distance_mi = distance_km / 1.609
print(distance_mi)
print("выведено значение дистанции в милях")


#Работа с числами 
print("новое задание:")
demo_int = int('215')
print(demo_int)

demo_float = float("215.3")
print(demo_float)

#абсолютное значение
print("новое задание:")
print(39 - 16)
print(16 - 39)

#abs - преобразование числа в абсолютное значение
print(abs(39 - 16))
print(abs(16 - 39))

#округление
print("новое задание: округлённые значения: ")
print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))

print("новое задание:")


#библиотека математических вычислений!

from math import ceil, floor
print('вывод с помощью ceil значения в большую сторону округления:')
round_up = ceil(12.5)
print(round_up)
print('вывод с помощью floor значения в меньшую сторону округления:')
round_down = floor(12.5)
print(round_down)


#решение задачек ( не выполнил, не работало) 
print("новое задание:")
first_planets_input = input('Введите значение дистанции от солнца к первой планете в км:')
second_planets_input = input('Введите дистанцию от солнца ко второй планете в км: ')
first_planets_input = int
second_planets_input = int
distance_kms = (int(second_planets_input)) - (int(first_planets_input))
print('вывод дистанции в абсолютном значении:')
print((distance_kms))
