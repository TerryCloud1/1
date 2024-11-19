x = 2  #целоечисло
print(type(x))  #<class 'int'>
print(x)
x = 2.5 #это число флоат 
print(type(x))  #<class 'float'>
print(x)
x = True #логический тип данных (bool) 
#True- 1 , False - 0/
print(type(x)) #<class 'bool'>

x = 'This is a string'
print(x) # это строка (a string)
print(type(x)) #вывод <class 'str'>
y = "This is also string"

#объединение строк
x = 'Hello' + ' ' + 'World'
print(x) #вывод Hello World
y = "Denis" + " " + "Backs"
print(y) #вывод 


#далее на выходные данные мини задачки
sum = 100 + 50 
print(sum)
print ("Показать это в консоле")

sum = 5 + 5 # 10
print(sum)
product = sum * 2  #20
print(product)

#Типы данных
#Числовой тип - int, float, complex, no = 3
#Текстовый тип - str = "a literal string"
#Тип Boolean(Логический) continue = True

planets_in_solar_system = 8 #int 
distance_to_alpha_centauri = 4.375 #float, lightyears
can_liftoff = True #bool
shuttle_landed_on_the_moon = "Apollo 11" #string
parsecs = distance_to_alpha_centauri /3.2

#решение пример световые года в парсеки
print(str(parsecs) + " Дистанция световых лет " 
      + str(distance_to_alpha_centauri) + " В парсеках ")


#определение типа данных
type(distance_to_alpha_centauri) ## <class 'float'>
type(planets_in_solar_system)
type(can_liftoff)
type(shuttle_landed_on_the_moon)




 
#работа с оператором (по центру деление как пример оператора)
 #операторы бывают: +, -, /, *
left_side = 10
right_side = 5
left_side / right_side #2 

#оператор присваивания :
# =  пример: x = 2
# += пример x += 2 
# -= пример x -= 2
# /= пример x/= 2 
# *= пример x *= 2 

#даты

from datetime import date
date.today()
print(date.today)

#чтобы всё работало, нужно преобразовать дату в строку
print("Today's date is: " + str(date.today()))

#массив sys
import sys
print(sys.argv)
print(sys.argv[0])

#работа с числами

print("программа калькулятор сложение")
first_number  = input("Первое число:")
second_number  = input("Второе число:")
print(int(first_number) + int(second_number))



