with open('sal.txt', 'r') as file:
    zp = []
    malozp = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
           malozp.append(i[0])
        zp.append(i[1])
print(f'Оклад меньше 20.000 {malozp} \n, средний оклад {round(sum(map(int, zp)) / len(zp))}')