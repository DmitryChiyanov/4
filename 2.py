spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
final = [spisok[num] for num in range(1, len(spisok)) if spisok[num] > spisok[num - 1]]
print(final)