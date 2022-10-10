
def ex1_cmmdc():
    a = int(input("Primul numar : "))
    b = int(input("Al doilea numar: "))
    c = int(input("Al treilea numar: "))
    while(b):
        a = b
        b = a % b
    while(c):
        a = c
        c = a % c
    return abs(a)

def ex2_vocale(string):
    vocale = 0
    for char in string:
        if char in "aeiouAEIOU":
            vocale = vocale + 1
    return vocale

def ex3(stringA, stringB) :
    return str.count(stringB, stringA)

def ex4(string):
    new_string = str(string[0]).lower()
    for char in string[1:]:
        if char in ('ABCDEFGHIJKLMNOPQERSTUVWXYZ'):
            new_string = str(new_string) + '_'
            new_string = str(new_string) + char.lower()
        else:
            new_string = str(new_string) + char
    return new_string

def ex6_palindrome(number):
    for i in range(0, int(len(str(number)) / 2)):
        if str(number)[i] != str(number)[len(str(number)) - i - 1]:
            return False
    return True

def ex7(string):
    number = ""
    for char in string:
        if char.isdigit():
            number = number + char
        elif number != "":
            return int(number)


def ex8(number):
    count = 0
    binary = format(number, "b")
    for char in binary:
        if char == '1':
            count = count + 1
    return count



def ex10(string):
    count = 0
    for char in string:
        if char == ' ':
            count = count + 1
    return count + 1



if __name__ == '__main__':
    print (ex1_cmmdc())
    print (ex2_vocale("casa"))
    print (ex3("bla", "blablabla"))
    print(ex4("CamelCaseEx"))
    print(ex6_palindrome(1234321))
    print(ex7("Printam numarul 123 si nu 78"))
    print (ex8(24))
    print(ex10("I have Python exam"))




