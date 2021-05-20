def factorio(chislo):
    start = 1
    if chislo == 0:
        yield f'{chislo}! = 1'
    for i in range(1, chislo+1):
        start *= i
        yield f'{i}! = {start}'

for el in factorio(int(input('введите число '))):
    print(el)
