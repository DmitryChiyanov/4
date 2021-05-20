from sys import argv

def zp():
    try:
        chas, stavka, prem = map(float, argv[1:])
        print(f"зарплата - {chas * stavka + prem}")
    except ValueError:
        print("вводить надо числа. 3 штука")

zp()