
def ex1_fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    lista = [0, 1]
    if n == 2:
        return lista
    for i in range(2, n):
        lista.append(lista[i-1] + lista[i-2])
    return lista


def ex2(lista):
    lista_prime = []
    for x in lista:
        if x == 2:
            lista_prime.append(x)
        if x > 2:
            for i in range(2, x):
                if x % i == 0:
                    break
                else:
                    lista_prime.append(x)
                    break
    return lista_prime



# intersectia, reuniunea, a-b, b-a
def ex3(a, b):
    intersectia, reuniunea, dif1, dif2 = [], [], [], []
    for i in a:
        for j in b:
            if i == j:
                intersectia.append(i)
                reuniunea.append(i)
                break
    reuniunea = a + b
    reuniunea = list(set(reuniunea))
    dif1 = list(set(a) - set(b))
    dif2 = list(set(b) - set(a))
    return intersectia, reuniunea, dif1, dif2



def compose(notes, moves, start) -> list:
    i = start
    song = []
    song.append(str(notes[i]))
    for j in range(0, len(moves)):
        if (i + moves[j]) < len(notes):
            i = i + moves[j]
        else:
            i = moves[j] - 1
        song.append(notes[i])
    return song


def ex5(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i > j:
                matrix[i][j] = 0
    return matrix


def ex6(x, *args):
    k=0
    lista = []
    items = []
    for arg in args:
        lista = lista + arg
    frecv = {}
    c = {}
    for i in lista:
        if i in frecv:
            frecv[i] += 1
        else:
            frecv[i] = 1

    for i in lista:
        c[i]=0

    for i in lista:
        if frecv[i] == x and c[i]!=1:
            items.append(i)
            c[i]=1
    return items

def ex7(numbers):
    nr = 0
    maxp = 0
    for i in numbers:
        ok = True
        for j in range(0, int(len(str(i)) / 2)):
            if str(i)[j] != str(i)[len(str(i)) - j - 1]:
                ok = False
        if ok:
            nr += 1
            if i > maxp:
                maxp = i
    return [nr, maxp]


def ex8(strings, x, flag):
    ascii_list = []
    for word in strings:
        word_list = []
        for i in word:
            if flag == True:
                if ord(i) % x == 0:
                    word_list.append(i)
            else:
                if ord(i) % x != 0:
                    word_list.append(i)
        ascii_list.append(word_list)
    return ascii_list


def ex9(matrix) -> list:
    spectators = []
    for i in range(1, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i-1][j] > matrix[i][j]:
                spectators.append((i,j))
    return spectators


def ex10(*args):
    max_len = 0
    t = ()
    lista = []
    for arg in args:
        if len(arg)> max_len:
            max_len = len(arg)

    for i in range(max_len):
        t = ()
        for arg in args:
            if i > len(arg) and len(arg) < max_len:
                t += ("none",)
            else:
                t += (arg[i],)
        lista.append(t)
    return lista


def ex11(string):
    for i in range(0, len(string)):
        for j in range(0, len(string) - i - 1):
            if(string[j][1][len(string[j][1])-1] > string[j+1][1][len(string[j+1][1])-1]):
                aux = string[j]
                string[j] = string[j+1]
                string[j+1] = aux
    return string





if __name__ == '__main__':
    print(ex1_fibo(8))
    print(ex2([2,4,6,7]))
    print(ex3([1,2,3,4], [2,4,6]))
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print(ex5([[1,2,3],[4,5,6],[7,8,9]]))
    print(ex6(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))
    print(ex7([1001,123,2332]))
    print(ex8(["test", "hello", "lab002"], 2, False))
    print(ex9([[1,2,3,2,1,1],[2,4,4,3,7,2],[5,5,2,5,6,4],[6,6,7,6,7,5]]))
    print(ex10([1,2,3],[5,6,7],["a","b","c"]))
    print(ex11([('abc', 'bcd'),('abc','zza')]))


