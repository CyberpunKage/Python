"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
a = "data\\task5.txt"

with open(a, "w", encoding="UTF-8") as f:
    b = input("Введите числа через пробел: ")
    f.writelines(b)
with open(a, "r", encoding="UTF-8") as f:
    c = f.read()
    print(sum([int(b) for b in c.split()]))
