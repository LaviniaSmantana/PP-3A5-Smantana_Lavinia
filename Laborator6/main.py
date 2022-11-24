import re
import os

def ex1(text):
    lista = []
    regex = "\s+"
    lista = re.split(regex, text)
    return lista

print("Exercitiul 1: ")
print(ex1("Un text cu cifre 123 si cuvinte"))


def ex2(regex, text, x):
    lista = []
    lista_x = []
    lista = re.findall(regex, text)
    for i in lista:
        if len(i) == x:
            lista_x.append(i)
    return lista_x

print("Exercitiul 2: ")
print(ex2("\d+", "Text 20 1234 abcdef 21 5392", 2))


def ex3(lista_strings, lista_reg):
    lista = []
    for i in lista_strings:
        ok = 0
        for r in lista_reg:
            if re.search(r, i):
                ok = 1
        if ok:
            lista.append(i)
    return lista

print("Exercitiu 3: ")
print(ex3(["Ana Are", "Mere", "12 2 5" , "nu apare in string"], ["\d+", "^A."]))


def ex6(text):
    new_text = ""
    lista_text = text.split(" ")
    for i in lista_text:
        if re.search("^[aeiouAEIOU].*[aeiouAEIOU]$", i):
            new_text = new_text + "*" + " "
        else:
            new_text = new_text + i + " "
    return new_text

print("Exercitiul 6: ")
print(ex6("Acesta este un text fara vocale la inceput sau sfarsit"))


def ex7(cnp):
    regex = "[5612]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$"
    if re.match(regex, cnp):
        return True
    else:
        return False

print("Exercitiul 7: ")
print(ex7("2960101123456"))


def ex8(director, regex):
    lista = []
    for current_path, directories, files in os.walk(director):
        for f in files:
            fisier = os.path.join(current_path, f)
            if re.search(regex, f):
                lista.append(f)
            try:
                with open(fisier, 'r') as file1:
                    if re.search(regex, file1.read()):
                        if re.search(regex, f):
                            lista[-1] = ">>" + lista[-1]
                        else:
                            lista.append(f)
            except:
                pass
    return lista

print("Exercitiul 8: ")
print(ex8("D:\\Lavinia\\FII3\\Sem1\\Python\\Laboratoare\\Laborator4", "\.txt$"))









