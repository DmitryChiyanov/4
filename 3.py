class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список, q для выхода')
        if value == 'q':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не число!')
print(my_list)

