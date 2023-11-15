'---------------------------Циклы------------------------------------'

# Циклы - это наш блок кода, которыый обрабатывает несколько раз
# 1. for - цикл , который работает до конца итерируемого обьекта 
 # 2 . while -  цикл, которые работает пока условие верно   (True)
# i = 1

# while i < 10:
#     print(f"Квадрат числа {i} = {i**2}")
#     # i = i + 1 
# i = 1
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(f"Квадрат числа {i} = {i**2}")
#     i = i + 1 




# text = 'Введите сообщения'
# text += "\n или введите словов exit для входа"

# answer = True
 
# while answer:
#     message = input(text)
#     if message == 'exit':
#         answer = False
#         print('Вы вышли из цикла')
#     else:
#         print(message) 




     



# for i in range(10):
#     print(i)



#     for i in range(10):
#         print(i + 1)

# for i in range(1, 11):
#   print(f"Квадрат числа {i} = {i**2}")

# for i in range(10):
#     print("Phyton is awesome!")
# i = 0
# while i < 10:
#     print("Python is awesome!")
#     i+=1 



# text = input('Напишите какой либо текст')
# # while text < 10:
# #    print(f"Напишите какой либо текст {text} = {text * 10}")

# count = int(input('Введите число повторении'))
# # while count < 10:
# #      print('Введите число повторении')

# i = 0
# while i < count:
#     print(text)
#     i +=1

# i = 0
# while i < count:
#     print(f'{text}: Отсчет на {1+1}')
#     i +=1



'--------------------------------- break and continue-----------------------------------------------'
# break  - оператор  который останавливает 
# continue - 




'------------------------Range------------------------------------------------------'
#range -  она позволяет нам  генерировать последовательность  чисел , в прамежутке указанного диапозона 


# for i in range(10):
#     print('Privet', 1)




#range (start, end  , step)
#for i in range(5 , 36 , 5):
#   print(i)



# Отрицательное шаг

# m = int(input("Введите число: "))
# n = int(input("Введите число: "))

# for i in range(m , n):
#     if i % 2 == 0:
#         print(i)

# num = int(input())
# if 7 in num:
#     print('Yes')
# else:
#     print('No')

# num =  int(input())
# has_seven = False

# while num != 0:
#     last_digit = num % 10
#     print(f'Наше текущее число:{num}')
#     if last_digit == 7:
#         has_seven = True
#         break
#     num = num // 10
# if has_seven:
#     print('YEs')
# else:
#     print('No')


# import time 
# for hours in range(24):
#     for minutes in range(60):
#         for seconds  in range(60):
#             time.sleep(1)
#             print(hours , ':' , minutes , ' :' , seconds)



