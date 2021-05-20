def summa():
    try:
        with open('file.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            chisla = line.split()

            print(sum(map(int, chisla)))

    except ValueError:
        print('цифра надо вводить')
summa()
