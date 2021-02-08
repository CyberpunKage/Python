"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента. Подсказка: элементы, удовлетворяющие
 условию, оформить в виде списка. Для формирования списка использовать генератор.
 """
"""
Функция в которой каждый элемент в диапазоне элеметов от 1 до n,
 где n это число элементов исходного списка, проходит проверку на условие, 
 "элемент больше предыдущего элемента?", если да, то вывести генератор. 
"""
def max_el(a):
    for el in range(1, len(a)):
        if a[el] > a[el-1]:
            yield a[el]

"""
b = исходный список значений
c = список в который добавляем значения элементов функции, удовлетворяющих условию,
"""

b = [14, 8, 17, 1, 2, 6, 5, 9]
c = []
for el in max_el(b):
    c.append(el)
print(c)
