def odd_even():
    liste = [1, 2, 3, 4, 5, 6]
    tek = []
    cift = []
    for i in liste:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    print(int(max(cift)) - int(min(tek)))


odd_even()
