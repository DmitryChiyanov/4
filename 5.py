class Stationary:

    def __init__(self, title="канц прибор"):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать используя {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'{self.title} это ручка')


class Pencil(Stationary):
    def draw(self):
        print(f'{self.title} это карандаш')


class Marker(Stationary):
    def draw(self):
        print(f'{self.title} это маркер')

stat = Stationary()
stat.draw()

mark = Marker()
pen = Pen()
pensil = Pencil()

mark.draw()
pen.draw()
pensil.draw()