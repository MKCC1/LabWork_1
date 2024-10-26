money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
# Вариант через обычный цикл
while money_capital + salary - spend >= 0:
    money_capital += salary - spend
    spend += spend * increase
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)


# Вариант через цикл с постусловием
# money_capital = money_capital + salary - spend #первый месяц без роста цен
# months = 1
#
# while True:
#     money_capital += salary
#     spend = spend * (1 + increase)
#     money_capital -= spend
#     if money_capital < 0: # Цикл с постусловием
#         break
#     months += 1
# print("Количество месяцев, которое можно протянуть без долгов:", months)
