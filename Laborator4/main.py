import os


def ex1(director):
    lista_extensii = []
    try:
        for file in os.listdir(director):
            if '.' in file:
                poz = file.find('.')
                lista_extensii.append(file[poz:])
        return lista_extensii
    except:
        print("Directory doesn't exist")

#print(ex1("D:\Lavinia\FII3\Sem1\Python\Laboratoare\Laborator4"))


def ex2(director, fisier):
    fisiere = []
    try:
        for file in os.listdir(director):
            fisiere.append(file)
    except:
        print("Directory doesn't exist")

    try:
        with open(fisier, 'w') as f:
            for c in fisiere:
                f.write(c + "\n")
            f.close()
        f = open(fisier, "r")
        print(f.read())
    except:
        print("File doesn't exist")

#print (ex2("D:\Lavinia\FII3\Sem1\Python\Laboratoare\Laborator4", "D:\Lavinia\FII3\Sem1\Python\Laboratoare\Laborator4\\test.txt"))


def ex3(my_path):
    if os.path.isdir(my_path):
        lista = []
        dict_extensii = {}
        try:
            for file in os.listdir(my_path):
                if '.' in file:
                    poz = file.find('.')
                    if file[poz:] in dict_extensii:
                        dict_extensii[file[poz:]] +=1
                    else:
                        dict_extensii[file[poz:]] = 1
        except:
            print("Directory doesn't exist")

        for i in dict_extensii.items():
            lista.append(i)
        return lista
    elif os.path.isfile(my_path):
        try:
            with open(my_path, 'r') as f:
                lista = f.read().replace('\n', ' ')
            return lista[-20:]
        except:
            print("File doesn't exist")

#print(ex3("fisier.txt"))


def ex4(director):
    lista = []
    dict_extensii = {}
    lista_extensii = []
    try:
        for file in os.listdir(director):
             if '.' in file:
                poz = file.find('.')
                lista_extensii.append(file[poz:])
                if file[poz:] in dict_extensii:
                    dict_extensii[file[poz:]] += 1
                else:
                    dict_extensii[file[poz:]] = 1
    except:
        print("Directory doesn't exist")

    for i in lista_extensii:
        if dict_extensii.get(i) == 1:
            lista.append(i)
    lista.sort()
    return lista

#print(ex4("D:\Lavinia\FII3\Sem1\Python\Laboratoare\Laborator4"))


def ex5(target, to_search):
    lista = []
    if os.path.isfile(target):
        try:
            with open(target, 'r') as f:
                if to_search in f.read():
                    return target
        except:
            print("File doesn't exist")
    elif os.path.isdir(target):
        try:
            for file in os.listdir(target):
                with open(file, 'r') as f:
                    if to_search in f.read():
                        lista.append(file)
        except:
            print("Directory doesn't exist")
    else:
        raise ValueError("Target-ul introdus nu este nici fisier, nici director.")

#print(ex5("D:\\Lavinia\\FII3\\Sem1\\Python\\Laboratoare\\Laborator4", "sunt"))

def ex7(string):
    dictionar = {}
    dictionar["full_path"] = os.path.abspath(string)
    dictionar["file_size"] = os.path.getsize(string)

    if '.' in string:
        poz = string.find('.')
        dictionar["file_extension"] = string[poz:]
    else:
        dictionar["file_extension"] = ""

    f = open(string, 'r')
    if f.readable():
        dictionar["can_read"] = True
    else:
        dictionar["can_read"] = False

    f = open(string, 'w')
    if f.writable():
        dictionar["can_write"] = True
    else:
        dictionar["can_write"] = False

    return dictionar

#print(ex7("fisier.txt"))


def ex8(dir_path):
    lista = []
    try:
        for file in os.listdir(dir_path):
            if os.path.isfile(file):
                x = dir_path + "\\" + file
                lista.append(x)
        return lista
    except:
        print("Directory doesn't exist")

#print(ex8("D:\\Lavinia\\FII3\\Sem1\\Python\\Laboratoare\\Laborator4"))