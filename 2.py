my_file = open('file.txt', 'r')
content = my_file.read()

print(f'Содержимое файла: \n {content}')

my_file = open('file.txt', 'r')
content = my_file.readlines()

print(f'Количество строк в файле - {len(content)}')

my_file = open('file.txt', 'r')
content = my_file.readlines()

for i in range(len(content)):
    print(f'Количество слов {i + 1} - ой строки {len(content[i].split())}')


my_file.close()