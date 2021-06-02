class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        num1 = int(input('введите делимое: '))
        num2 = int(input('введите делитель: '))
        if num2 == 0:
            raise OwnError('На ноль делить нельзя! Бан!')
        else:
            result = round(num1 / num2, 2)
            return result
    except ValueError:
        return "Вы не ввели число! Бан!"
    except OwnError as err:
        return err


print(div())

