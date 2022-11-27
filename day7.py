def string_range():
    x = int(input("bir sayı giriniz : "))
    a = 0
    while a < x:
        print(a, end="")
        a = a + 1
        if a == x:
            break
        print(".", end="")


string_range()
