#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("Введите число: "))
a = str(n) + str(n)
b = str(n) + str(n) + str(n)
E = n + int(a) + int(b)
Out = f'{n}+{a}+{b}={E}'
print(Out)
