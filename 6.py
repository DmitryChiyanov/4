from itertools import count, cycle



print('итератор, генерирующий целые числа, начиная с указанного, выход = Q')
for i in count(int(input('введите начальное число '))):
    print(i, end='')
    quit = input()
    if quit == 'Q':
        break

print(' итератор, повторяющий элементы некоторого списка, определенного заранее, выход = Q')
spisok = input('введите числа через пробел ').split()
iter_ = cycle(spisok)

for i in count(1):
    print(next(iter_), end='')
    quit = input()
    if quit == 'Q':
        break