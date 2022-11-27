def equal_strings(a, b):
    x = []
    for i in a:
        x.append(i)
    y = []
    for i in b:
        y.append(i)
    x.sort()
    y.sort()
    if x == y:
        print("True")
    else:
        print("False")


equal_strings('love', 'evol')
