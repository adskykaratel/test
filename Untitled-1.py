# Запрос варианта задания
variant = int(input("Введите номер варианта задания (от 1 до 12): "))

# # В зависимости от варианта выбора пользователя, выполняем соответствующее задание
if variant == 1:
    name = input("Ваше имя? ")
    birthdate = input("Ваша дата рождения? ")
    education = input("Где Вы учитесь? ")
    print("Ваше имя:", name)
    print("Дата рождения:", birthdate)
    print("Вы учитесь в", education)

# elif variant == 2:
# surname = input("Ваша фамилия? ")
# residence = input("Где Вы живете? ")
# print("Ваша фамилия:", surname)
# print("Вы живете в", residence)

# ... Продолжайте аналогично для всех вариантов задания

else:
    print("Неверный номер варианта задания. Введите число от 1 до 12.")

# Контрольные вопросы можно также задать пользователю или включить их в текст заданий.