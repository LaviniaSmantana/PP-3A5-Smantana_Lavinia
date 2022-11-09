
print("Exercitiul 2: ")
def ex2(*args, **kwargs):
    suma = 0
    for i in kwargs.values():
        suma += i
    return suma

print(ex2(1, 2, c=3, d=4))

# anonymous function = lambda function
print("Exercitiul 2 cu anonymous function: ")
anon_ex2 = lambda *args, **kwargs: sum(kwargs.values())
print(anon_ex2(1, 2, c=3, d=4))



lista_ex3 = "Programming in Python is fun"
def ex3(string):
    lista = []
    for c in string:
        if c in 'aeiouAEIOU':
            lista.append(c)
    return lista
print("Exercitiul 3: ")
print(ex3(lista_ex3))

print("Exercitiul 3 - anonymous function with filter: ")
print(list(filter(lambda x: x[0] in "aeiouAEIOU", lista_ex3)))

print("Exercitiul 3 - list comprehension: ")
vocale = [i for i in lista_ex3 if i in 'aeiouAEIOU']
print(vocale)



def ex4(*args, **kwargs):
    lista = []

    for arg in args:
        if isinstance(arg, dict):
            argument = arg.copy()
            keys = 0
            keys_with_3c = 0
            for key, val in argument.items():
                keys += 1
                if len(str(key)) >= 3:
                    keys_with_3c += 1
            if keys >= 2 and keys_with_3c >= 1:
                lista.append(argument)

    for key, val in kwargs.items():
        if isinstance(val, dict):
            kwarg = val.copy()
            keys = 0
            keys_with_3c = 0
            for k, v in kwarg.items():
                keys += 1
                if len(str(k)) >= 3:
                    keys_with_3c += 1
            if keys >= 2 and keys_with_3c >= 1:
                lista.append(kwarg)
    return lista

print("Exercitiul 4: ")
print(ex4( {1: 2, 3: 4, 5: 6},
 {'a': 5, 'b': 7, 'c': 'e'},
 {2: 3},
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}))



def ex5(lista):
    new_list = []
    for i in lista:
        if isinstance(i, int):
            new_list.append(i)
        elif isinstance(i, float):
            new_list.append(i)
    return new_list

print("Exercitiul 5: ")
print(ex5([1,"2", {"3":"a"}, {4,5}, 5, 6, 3.0]))



def ex6(lista):
    lista_odd = []
    lista_even = []
    new_list = []
    for i in lista:
        if i%2 == 0:
            lista_even.append(i)
        else:
            lista_odd.append(i)
    for i in range(0, len(lista_even)):
        t = (lista_even[i], lista_odd[i])
        new_list.append(t)
    return new_list

print("Exercitiul 6: ")
print(ex6([1,3,5,2,8,7,4,10,9,2]))



print("Exercitiul 7: ")
def ex7(**kwargs):
    fibo = [0, 1]
    for i in range(2, 1000):
        fibo.append(fibo[i-1] + fibo[i-2])

    if "filters" in kwargs.keys():
        fibo = [i for i in fibo if all([f(i) for f in kwargs["filters"]])]
    if "offset" in kwargs.keys():
        x = kwargs["offset"]
        fibo = fibo[x:]
    if "limit" in kwargs.keys():
        x = kwargs["limit"]
        fibo = fibo[:x]
    return fibo

def sum_digits(x):
    return sum(map(int, str(x)))
print(ex7(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))



print("Exercitiul 8 a) : ")

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def argumente(*args, **kwargs):
    print(args, kwargs)

def print_arguments(function):
    def argumente_wrapper(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)
    return argumente_wrapper

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)


print("Exercitiul 8 b) :")

def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    def arg_wrapper(*args):
        return 2 * function(*args)
    return arg_wrapper

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)
print(x)