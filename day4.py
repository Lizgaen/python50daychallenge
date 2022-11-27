def only_floats(d, c):
    fl = 0
    if type(d) == float:
        fl = fl + 1
    if type(c) == float:
        fl = fl + 1
    print(fl)


only_floats(2, 2.3)
