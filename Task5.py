#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
x = int(input("Ведите выручку фирмы: "))
y = int(input("Введите издержки фирмы "))
if x > y:
    print("Фирма прибыльна")
    r = ((x - y) / x) * 100
    print("Рентабельность: ", int(r), "%")
    n = int(input("Пожалуйста, введите количество сотрудников фирмы: "))
    r = (x - y) / n
    print("Прибыль на одного сотрудника равна: ", int(r))
else:
    print("Фирма убыточна")