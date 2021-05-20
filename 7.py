import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'средняя прибыль - {prof_aver:.2f}')
    else:
        print(f'денег нет но вы держитесь')
    pr = {'srednyaya pribil': round(prof_aver)}

    print(f'Прибыль каждой компании - {profit}')

with open('file.json', 'w') as write_js:
    list = [profit, pr]

    json.dump(list, write_js)
