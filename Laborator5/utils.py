def process_item(x):
    if x == 1:
        return x + 1
    prim_x = x
    prim_gasit = 0

    while prim_gasit == 0:
        prim_x += 1
        ok = 1
        for i in range(2, prim_x):
            if prim_x % i == 0:
                ok = 0
                break
        if ok == 1:
            prim_gasit = 1
            return prim_x

