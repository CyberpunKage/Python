"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
"""
Модуль time - модуль для работы со временем в Python.
"""
import time


"""
Создаём класс TrafficLight, атрибуты устанавливаем приватными (__)
Метод running запускает цикл, который остановится после 10 выводов.
В цикле организован перебор элементов списка светофора, и исходя из значения элемента,
выводится соответствующее сообщение, time.sleep() устанавливает задержки посекундно.
Коды в print задают цвет текста. В итоге создаем экземпляр класса, вызываем метод.
"""
class TrafficLight:
    __color = ["red", "yellow", "green"]
    __counter = 0
    def running(self):
        while True:
            for el in self.__color:
                if el == "red":
                    print(f"\033[31m {el}")
                    time.sleep(7)
                elif el == "yellow":
                    print(f"\033[33m {el}")
                    time.sleep(2)
                else:
                    print(f"\033[32m {el}")
                    time.sleep(4)
                self.__counter +=1
                if self.__counter == 10:
                    print("Конец перебора")
                    break
            if self.__counter == 10:
                break

a = TrafficLight()
a.running()
