'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def transfuse(cls, a):
        day, month, year = map(int, a)
        res = cls(day, month, year)
        print(f'\033[38m Результат работы классового метода: {day}.{month}.{year}\n Тип даты: {type(day)}')
        #Хотел вернуть res для последующей обработки в статическом методе, но повис)
        return res

    @staticmethod
    def validate(a):
        day, month, year = map(int, a)
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 2030:
                    print('\033[38m Дата введена верно')
                else:
                    print('\033[31m Год ввёден не верно')
            else:
                print('\033[31m Месяц введён не верно')
        else:
            print('\033[31m День введён не верно')


inp_date = Date.transfuse([str(i) for i in input('\033[38m Введите число, месяц и год через дефис: ').split('-')])
inp_valid = Date.validate([str(i) for i in input('\033[38m Введите число, месяц и год через дефис для проверки валидации: ').split('-')])
