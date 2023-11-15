# def eat(food):
#     text = f'i eat {food}'
#     return text


# def animal(get_voice):
#     text = f'mu mu mu {get_voice}'
#     return text


# a = lambda: print("hello")
# a()



# my_list = [1,10,3,5,100]
# even_list = list(filter(lambda a: a%2==0 ,my_list))
# print(even_list)

'-------------------------Рекурсивная функция ---------------------'

# это функция вызывает сама себя в теле своей раелизации    
#  Основные характеристики рекурсивных фугкции ;


'1. Базовый случай - Функция должна иметь условия выхода'

'2.Рекурсивный случае - Внутри функции должен быть вызов самой функции, но уже с измененным параметром'




def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number -1)
    
print(factorial(995))


