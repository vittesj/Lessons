'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
 Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
 выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    def __init__(self):
        self.title = 'название'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print('Запуск отрисовки инструментом: ' + self.title)


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print('Запуск отрисовки инструментом: ' + self.title)


class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        print('Запуск отрисовки инструментом: ' + self.title)


text_1 = Stationery()
text_1.draw()
text_2 = Pen()
text_2.draw()
text_3 = Pencil()
text_3.draw()
text_4 = Handle()
text_4.draw()
