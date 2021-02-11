"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад
менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
"""
a = "data\\task3.txt"
"""
Читаем файл и присваиваем строки переменной "с", 
"""
with open(a, "r", encoding="UTF-8") as b:
    c = b.readlines()
name = []
stonks = 0
for el in c:
    sec_name, money = el.split(" - ")
    money = int(money)
    stonks += money
    if money < 20000:
        name.append(sec_name)
print(f"Сотрудники < 20k: {name}")
print(f"Средний доход: {stonks / len(el)}")
