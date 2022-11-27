from math import sqrt


def divide_or_square():
    sayi = int(input("sayi giriniz : "))
    if sayi % 5 == 0:
        print(sqrt(sayi))
    else:
        print(sayi % 5)


divide_or_square()
