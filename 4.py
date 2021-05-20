
rus = {'One' : 'один', 'Two' : 'два', 'Three' : 'три', 'Four' : 'четыре'}
new_file = []
with open('file.txt', 'r') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
