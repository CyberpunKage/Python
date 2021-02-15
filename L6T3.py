"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        """
        для работы с атрибутами родителя пишем super().__init__
        """
        super().__init__(name, surname, position, income)

    def f_name(self):
        return f"{self.surname} {self.name}"

    def f_income(self):
        return self._income.get("wage") + self._income.get("bonus")

a = Position(name="Константин", surname="Боронин", position="Студент", income={"wage": 35000, "bonus": 10000})
print(a.f_name())
print(a.f_income())
