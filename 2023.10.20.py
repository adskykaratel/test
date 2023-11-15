# '----------------------int---------------------------'

# # a = 5
# # print(a)
# # print(type(a))

# # b = int('17')
# # print(b)

# '------------------------float-----------------------------'

# # c = 1.5
# # print(type(c))

# # print(a +c)


# # from decimal import Decimal
# # a = Decimal('0.1')
# # print(a+a+a+a+a+a+a+a+a+a)


# '--------------------------Операции над числами--------------------------'
# 5 + 9   #Сложения
# 9 - 5   #Вычетания
# 9 * 5   #Умножения
# 10 / 2  #Деления
# 7 // 2  #деление, без остатка
# 5 % 2   #деление, остаток от деление 
# 2 ** 3  #возведение в степень
# 25 ** 0.5 #нахождение квадратного корня числа


# # a = input("Число a: ")
# # b = input("Число b: ")
# # if a > b:
# #     print("Число a больше " + a)
# # elif a < b:
# #     print("Число b больше " + b)
# # else:
# #     print("Числа равны a = b ")


# #модуль числа = положительное число |-5|=5
# # print(abs(-5))
# #roud = округление числа
# # print(round(6.5))
# # print(round(5.4))
# # print(round(5.1676437634, 3)) #print(round(5.1676437634, 3)) = 5.168




# # from math import sqrt

# # print(sqrt(125))



# #pow
# #1. Возодит в степень
# #2. Находит остаток от деления на 3 числа

# # print(pow(2,3,4)) # 2**3%4


# '--------------------------------------------- < > = ---------------------------------------------------'
# # ==равенсто
# print(5==5)
# print(4==5)

# #не равенство
# print(5!=5) #False
# print(4!=5) #True

# #больше                      #больше или равно
# print(5>4) #True             #5>=5 true
# print(3>4) #False            #5>= False

# #менше                       #менше или равно
# print(7>9) #False            #5<=5 True
# print(8<9) #True             #5<=4 False


# # import math
# # print(math.pi)

# # import random
# # print(random.random)
# # print(random.choice([i for i in range(1,11)]))




# a = 2.1
# b = 2.1
# c = 2.1
# print((a + b) * c)



# a = 6
# b = 5
# c = 15.5
# d = 7
# e = 5

# print((a - e** (b / d)) % c)



# print(a > b < c)
# print(abs(7 % 3) * 4.8)
# print(5 == 5)
# print(4 == 5)

# t = -21//10
# print(t)



# a = 2005
# b = 2023
# age = a - b
# print(age)
# print(age + 2)
# print(age - 2)
# print(age * 365)

# a = 10
# b = 15
# c = 75
# d = 20
# m = (a+b+c+d)/4
# print(m)

# l = 1*2*3*4*5*6*7*8*9*10
# print(l)

# print(m == l)

# a = 33 > 32
# b = 4 >= 2
# c = 2 == 2

# seconds_in_minutes = 60
# minutes_in_hours = 60
# hours_in_day = 24
# day_in_year = 365
# age = 18

# seconds_in_hours = seconds_in_minutes * minutes_in_hours

# seconds_in_day = hours_in_day * seconds_in_hours

# seconds_in_year = day_in_year * seconds_in_day

# seconds_in_my_age = age * seconds_in_year

# print(seconds_in_my_age)


#10, 12, 13, 100, 134567 Ввести  на input
# num = int(input("Введите число: "))
# if num % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")


# name = "Айтибек"
# weight20 = 75
# weight21 = weight20 + 5
# weight22 = weight21 + 10
# weight23 = weight22 - 20

# weight = abs(weight20 - weight23)
# print(weight)


# chocolate = 3
# milk = 2
# coffe = 1

# sum_chocolate1 = 5 * chocolate
# sum_milk1 = 3 * milk
# sum_coffe1 = 2 * coffe

# sum = sum_chocolate1 + sum_milk1 + sum_coffe1
# print(sum)


# a = 5
# b = a * 3
# c = a + b 


# a = 10
# b = 5
# S = (a*b)/2
# print(S)



# P = a+b+c+d
# print(P)

# c = 34
# f = c * 1.8 + 32 # c*2+30 = не точный но быстрый вариант.
# print(f)

# a = 3
# b = 5
# c = ((a+b)*2)/(b-a)
# print(c)


# d = int(input())
# e = 2
# g = e**(d)

# if c == g:
#     print("True")
# else:
#     print("False")

# a = 10
# b = 4
# s = (a*b)/2
# print(s)


# notebook_price = 50000
# discount = 10
# sum = (100 - discount) * notebook_price // 100
# print(sum)

# burger_price = 50
# markup = 100
# price = (100 + markup)* burger_price //100
# print(price)







#___________-----------------_______-----------------------_-----------__-----_--------__--_---_--------_---_--------_----_---_----_--------_---_---_---_---__------_---_----_-------------------------------_---

# Строки Strings .Строки .Форматирование строк. Строкые методы 
#-------------------------------------------------------String()----------------------------------------------------------
# строки - неизменяимый тип данных , который предназначен для работы с тексттом и его хранения (последовательность символов)
# заключенный в одинарные либо в двойные кавычки "" or ''
  

# string1 ='строка "с" одинарными кв'
# string2 = "строка 'с' двойными кавычками"
# string3 =  "Don\'t" # обратный слеш подсказывает питону что после него идет символ кавычки
# string4 = """
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# """ #Много строчный текст в этом тексте можно ставить любые кавычки 
# string5 = "hello " + ' ' + 'world' # конкентанация
# print(string5)
# s1 = 'ab'+ 'bc'
# s2 = 'bc' + 'ab'
# print(s1, s2)

# print('a' , 'b' , 'c' sep='*' , end="!") #  вместо того что бы так длинно писать мы можем его укоротить 
# print('a' + '*' + 'b' + '*' + 'c' + '!' ) 




# s3 = 'hi' * 4
# print(s3)
# print('-'*72)
# print('Ada')
 
# """Напишите программу , которая выводит текст:
# "Python is a great language!" , said Fred. "I don't ever remember having this much fun before.""""
# s= '"Python is a great language!" , said Fred. " I don'+" ' " + 't ever remember having this much fun before."'


# print(s)

"-------------------------------------------Экранизация строк---------------------------------------------"

# '\n' # перенос на новую строку
# print("Privet \nAndrey")
# '\t' #табуляция
# print('Hello\tworld')
# '\'' #jотоброжение кавычки
# "\"" #отоброжение двойной кавычки
# '\\' #отоброжения одного слеша
# print('Hello \\world')
# '\v' #перенос строки на новую со смещенеием вправо на длинну предыдущей строки
# print('hello\vworld\vada\vcourses')

"----------------------------Форматирования строк--------------------------------------"


# title = 'Iphone 15'
# price = '1000$'
# print('-'*72)
# format1 = f'Название товара: {title}\nЦена: {price}'
# print(format1)
# print('-'*72) 
# format2 = "Название товара: {}\nЦена: {}  {}шт" 
# print(format2.format("Хлеб", 100 , 3))
# print('-'*72)
# format3 = "Название товара: %s\nЦена: %s"
# print(format3 % ('Mac' , 1500))
# print('-'*72)

"------------------------------------Функция Len()---------------------------------------------------------"
# len()- считает количевство символов в строке 

# string1 = 'Hello world'
# count = len(string1)
# print(type(count))


#input("Введите команду")
#print(len(int))



# a = input('Название футбольной команды: ')
# count = len(a)
# format1 = f'Footbal club: {a}\nИмеет длину: {count}'
# print(format1)
# print('-'*72)

# b = input('Название футбольной команды: ')
# count = len(b)
# format1 = f'Footbal club: {b}\nИмеет длину: {count}'
# print(format1)
# print('-'*72)

# c = input('Название футбольной команды: ')
# count = len(c)
# format1 = f'Footbal club: {c}\nИмеет длину: {count}'
# print(format1)
# print('-'*72)






"-----------------------------------------Оператор in  в питоне-----------------------------------------------"
# В питоне есть специальный оператор который позволяет проверить, что одна строка находится внутри другой ,


# string1 = input()
# if 'a' in string1:
#if 'v' in string1:
#     print("В твоей строке присутствует символ а")
# else:
#     print('nope')

# string1 = input("Введите пароль")
# if len(string1) >=5 and 'qwerty'   not in string1:
#     print("Ваш пароль сахранен")
# else:
#     print("Ваш пароль ненадежный")


# string1 = input()
# if 'синий' in string1:
#     print('YES')
# else:
#     print("No")


"-------------------------------------------------Индексы------------------------------------------"
# индексы - порядковые номера элемента в последовательности (символ в строке) , Отчет начинается с  0  1  2  3  4  5 .....


# """
# H e l l o     W o r l d 
# 0 1 2 3 4 5 6 7 8 9 10 11 """

# срез - это определенная часть строки 
 # string[start, end, steps]
# string1 = "Hello world"
# print(string1[:: -1 ])
# print(string1[5 :])

"--------------------------------------------мЕТОДЫ СТРОК-----------------------------------------------------------"
# мЕТОДЫ - функции которые относятся к определенному классу (типу данных) , к ним обращемся через #  через точку 


# string1 = ' helloworld'
# print(string1.upper())

# print('qweqweq'.upper()) #все буквы переводит в вехнии регистр

# print(string1.lower())  #все маленькие буквы

# print(string1.swapcase())  #меняет регистр всех букв

# print(string1.little())  #каждое слово будет с большой буквой

# print(string1.capitalize())  #делает первую буквы большой  а остальные маленькой 

# print(string1.count('l')) #считает символы

# print(string1.startswith('el')) # проверка начинается ли строка с задданых символов

# print(string1.endswith('old')) # проверка заканчивается ли строка с заданных символов

# print(string1.isupper()) #проверка на верхнии регистр

# # print(string1.islower()) #проверка на нижнии регистр

# # print(string1.isdigit()) #проверка является ли строка числовой

# # print(string1.isalpha()) # проверка является ли строка буквами

# # print(string1.isalnum()) #является ли строка буквами числами или все вместе 

# # print(string1.split()) #разделитель  

# # print(''.join(['world',string1])) #склеивает в строку 

# # print(string1.strip()) #убирает символы в строке в том числе и пробел , действует только в начале 

# # string1 = '-------.Addaaaa'
# # print(string1.strip('-.a')) #убирает с начало и конца 

# # print(string1.lsstrip()) #убирает символы слева

# # print(string1.rstrip()) #убирает символы справа 

# # print(string1.replace('l',' ')) #меняет символ на указанный 



# # num = 13
# # # print(type(str(num)))

# # number = input()
# # n1 = int(number[0])
# # n2 = int(number[1])
# # n3 = int(number[2])
# # n4 = int(number[3])
# # if n1 + n4 == n2 - n3:
# #     print('YES')
# # else:
# #     print('NO')

# # a = 1 * -1

# # # print(a)
# # for x in range(1):
# #  print(x)


# # a = input(' Ваш электронный адрес')
# # if "@" in a and "." in a :
# #     print('YES')
# # else:
# #     print('NO')



# a = input()
# b = input()
# c = input()
# a_count = len(a)
# b_count = len(b)
# c_count = len(c)

# if a>b and a>c:
#   print(f"{a} Больше других")
# elif b>a and b>c:
#   print(f"{b} Больше других")
# elif c>a and c>b:
#   print(f"{c} Больше других")

# if a<b and a<c:
#   print(f"{a}Меньше других")
# elif b<a and b<c:
#   print(f"{b} Меньше других")
# elif c<a and c<b:
#   print(f"{c} Меньше других")


