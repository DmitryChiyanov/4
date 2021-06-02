class Error:
    def __init__(self):
        self.my_list = []

    @property
    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter. Для выхода пропишите чит-код 1109. '))
                if val != 1109:
                    self.my_list.append(val)
                    print(f'Текущий список - {self.my_list} \n ')
                else:
                    print('пока! Итоговый список: ', (self.my_list))
                    break

            except:
                print(f"Недопустимое значение - строка и булево")
                exit_try = input(f'Попробовать еще раз? Y/N')

                if exit_try.lower()== 'y':
                    print(try_except.my_input)
                elif exit_try.lower()== 'n':
                    return f'итоговый список: {self.my_list}'
                else:
                    return f'пошел отседова....'



try_except = Error()
print(try_except.my_input)
