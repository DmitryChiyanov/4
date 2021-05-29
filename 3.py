class Kletka:

    def __init__(self, num:int):
        self.num = num

    def __str__(self):
        return '*' * self.num

    def __add__(self,next):
        return Kletka(self.num + next.num)

    def __sub__(self, next):
        if self.num < next.num:
            print("Нельзя вычесть из маленькой большую")
            return self
        return Kletka(self.num - next.num)

    def __mul__(self, next):
        return Kletka(self.num * next.num)

    def __truediv__(self, next):
        if self.num < next.num:
            print('низя так, глупый')
            return self
        else:
            return Kletka(self.num // next.num)

    def make_order(self, num_in_row:int):
        return '\n'.join(['*' * num_in_row for _ in range(self.num // num_in_row)]) + '\n' + '*' * (self.num % num_in_row)


a = Kletka(10)
b = Kletka(5)
c = Kletka(27)
print(c.make_order(5))
print('-' * 20)
print(a-b)
print(a+b)
print(a/b)
print(a*b)