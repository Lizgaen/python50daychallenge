def register_check():
    register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
    sayi = 0
    for i in register:
        if register[i] == "yes":
            sayi = sayi + 1
        else:
            continue
    print(sayi)


register_check()
