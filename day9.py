def biggest_odd():
    x = str(input("sayi giriniz : "))
    liste = []
    for i in x:
        if int(i) % 2 == 1:
            liste.append(i)
    print(max(liste))


biggest_odd()
