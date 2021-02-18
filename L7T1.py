'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        # х - строковый тип, для каждого элемента el в матрице добавляем в х через пробел элементы i -> i(el)
        # тем самым выводим элементы из списка в строку, после каждго el переход на новую строку \n для визуального построения матрицы.
        x = ''
        for el in self.matrix:
            x += f'{" ".join([str(i) for i in el])}\n'
        return x

    def __add__(self, other):
        # IndexError: list index out of range чтобы избежать этой ошибки, пришлось создать список с диапазоном
        y = [[] for el in range(len(self.matrix))]
        # Для каждого элемента i в диапазоне элементов матрицы создаем свой перебор элементов j в диапазоне элементов матрицы от [i],
        # добавляем новому списку сумму элементов a и b (1 элемент первой матрицы + 1 элемент второй матрицы)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                y[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(y)


a = Matrix([[21, 44, 82], [15, 10, 7], [0, 55, 2]])
b = Matrix([[18, 4, 3], [25, 30, 29], [72, 22, 2]])
print(f' Матрица 1:\n{a}')
print(f' Матрица 2:\n{b}')
c = a + b
print(f' Сумма матриц:\n{c}')