from abc import ABC, abstractmethod

class Odezhda(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @property
    @abstractmethod
    def potreblenie(self):
        pass


    def __add__(self, next):
        return round(self.potreblenie + next.potreblenie, 3)


class Palto(Odezhda):

    @property
    def potreblenie(self):
        return self.parametr / 6.5 + 0.5


class Kostum(Odezhda):

    @property
    def potreblenie(self):
        return (2 * self.parametr + 0.3) / 100


kost = Kostum(220)
palto = Palto(58)
print(palto.potreblenie)
print(kost.potreblenie)
print(kost + palto)
print(palto.__add__(kost))

#в принципе, тут то вопросов нет, но как сюда можно было бы применить сеттер? Для одного класса
#это было в методичке, но у нас тут не один класс. Можете в коммите советик дать?