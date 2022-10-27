
def ex1(a, b):
    lista = []

    reuniune = a.union(b)
    lista.append(reuniune)

    intersectie = a.intersection(b)
    lista.append(intersectie)

    dif1 = a.difference(b)
    lista.append(dif1)

    dif2 = b.difference(a)
    lista.append(dif2)

    return lista


def ex2(string) :
    dictionar = {}
    for char in string:
        dictionar[char] = 0

    for char in string:
        dictionar[char] += 1

    return dictionar


def ex3(dictionar1, dictionar2):
    extra_items = set(dictionar1.items()).symmetric_difference(set(dictionar2.items()))
    if len(extra_items) != 0:
        return False
    else: return True



def build_xml_element(tag, content, href, _class, id):
    string_xml = "<" + tag + " href=\\"+ href + "\ \"_class=\"" + _class + "\" id=\"" + id + "\">" + content + "</" + tag + ">"
    return string_xml


def ex6(lista):
    t = ()
    unique_elements = set(lista)
    nr_of_unique = len(unique_elements)
    t = t + (nr_of_unique,)

    duplicate_elements = len(lista) - len(unique_elements)
    t = t + (duplicate_elements,)
    return t


def ex9(*args, **keyargs):
    lista_pos_args=[]
    lista_keyw_args=[]
    lista=[]
    for arg in args:
        lista_pos_args.append(arg)

    for key, value in keyargs.items():
        lista_keyw_args.append(value)

    lista = set(lista_pos_args).intersection(set(lista_keyw_args))
    return len(lista)


if __name__ == "__main__":

    print(ex1({1,2,3}, {3,4,5}))
    print(ex2("Ana has apples"))
    print(ex3({"A" : 1, "B" : 2}, {"A" : 2, "B": 3}))
    print(build_xml_element("a", "Hello there", "http://python.org", "my-link", "someid"))
    print(ex6([1,2,3,1]))
    print(ex9(1,2,3,4, x=1, y=2, z=3, w=5))