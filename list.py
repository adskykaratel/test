# '----------------------------Лист---------------------------------------'
# # списки - именяемый тип данных ,т индексируемый , упорядночный, итерируемый , предназначенный для хранения любых данынх в определенном порядке 

# list1 = [ 1,2 ,3,4 ,'Hello', None , True, ['a','b','c']]
# print(list1[4])
# print(list1[-1][1])

# list2 = list('ada') #с помомщью этог=й функции мы можем создать или переобразить из других  типов данных новый лист 
# print(list2)
# list3 = list(range(101)) # range - генерация какого - либо диапозона числа с сохронением их в листе 
# print(list3)
# list4 = list2 + list3  #сложение дву листов приводит к слиянию всеех элементов в один лист 
# print(list4)
# list5 = [1,2,3] * 5 # умножение, создает одинаковые элеементы на число множителя 
# print(list5)



# count_list3 = len(list3) # фунуция лен находит количевство элементов в листе
# print(count_list3)









'-----------------------------Методы листа--------------------------------------------------'

# append -  добавляет элементы в наш лист , в конце списка

# list1 = []
# list1.append("Hello")
# print(list1)


# #pop - удаляет элемент мз списка по индексу и возвращает этот удаленный элемент б  если не указать индекс то он будеет удалять самый последныц элемент в списке
# # list1.pop(2)
# # print(list1)


# # # remove- удаляет элемент из списка по  значению

# # list1.remove("Hello")
# # print(list1)

# # count-  считает количевство принятого элемента  в списке 

# # a = list1.count(1)
# # print(a)



# #index -  вщзвращает индекс первого вхождения принятого элемента

# print(list1.index("Hello"))

# #insert - добавляет в список по индексу
# list1.insert(0,True)
# print(list1)


# #extend - расширяет список засчет другого списка
# list1 = [0,0,0]
# list2 = [1,1,1]
# list1.append(list2)
# print(list1)
# list1.extend(list2)
# print(list1)


# #revers - изменяет список раставляя его элементы в обртном порядке
# list1 (1,2,3,4,5,6)
# list1.reverse()
# print(list)
#  #sort - сортирует список, состоящий из одного типа данных
# list1 =[2,3,1,5,6,7,8,11,10]
# list1.sort(revers =  True )
# print(list1)


# #clear - очищает список 
# list1.clear()
# print(list1)


# name , age , prof = ['Eldos' , 19 , "Future developer"]
# # print(name,age,prof)



# n = int(input(''))
# list1 = list(range(1 , n+1))
# # print(list1)
# total = 0 
# for number in [1,2,3,4,5,6,7,8,9,99]:
#     total = total + number
# print(f'Сумма всех цифр из списка: {total}')


#list1 = [12,1 ,1,1,2,3,4,5,6,1,1,2,33]

# count_list1 = len(list1)
# list2 = list1.copy()
# # while 1 in list1:
# #     list1.remove(1)
# # print(list1)


# for i in list2:
#     if  i ==1:
#         list1.remove(i)
# print(list1)


'----------------------------------Встроеннные функции sum() , min() , max()----------------------------------------------------------'

# # встроенная функция примает в качестве параметра список  и ввычисляет его сумму элементов 
# numbers = [1,233,4,5,6,7,8,10]
# # print('Сумма всех элементов=', sum(numbers))



# #встроенная функция min() and max() принимает в качестве параметров список и находит минимальный и максимальный элемент в списке 
# print(min(numbers) , max(numbers) )





# '-----------------------------------------------Кортеж------------------------------------------------------------------------------------'
# tuple_ = (1,2,3)# Кортеж
# print(type(tuple_))
# tuple_1 = (1) #int
# print(type(tuple_1))


# tuple_2 = tuple('Hello world')
# print(type(tuple_2))


# tuple_count = len(tuple_2)
# print(tuple_count)

# a = int(input())
# spisok_slov = []
# for _ in range(a) :
#     text = input('Введите строку ')
#     spisok_slov.append(text)

# print(spisok_slov)