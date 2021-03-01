'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''
class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.с = 'a + b * i'

    def __add__(self, other):
        return f'Сумма с1 и с2 равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение с1 и с2 равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


с1 = Complex(3, -4)
с2 = Complex(7, 9)
print(с1)
print(с1 + с2)
print(с1 * с2)
