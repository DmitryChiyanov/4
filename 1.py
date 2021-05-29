uno = [[7,6,5,1],[8,4,9,2],[5,3,7,4]]
dos = [[1,2,3,4], [3,6,3,8],[2,8,5,3]]

class Matrixxx:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str,self.lists))

    def __add__(self, next):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + next.lists[i][j])
        return '\n'.join(map(str, c))

matrixx1 = Matrixxx(uno)
matrixx2 = Matrixxx(dos)


print(matrixx1 + matrixx2)
