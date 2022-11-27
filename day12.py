def count_dots():
    x = input("noktalı metin : ")
    n = 0
    for i in x:
        if i == ".":
            n = n + 1
    print("." * n)


count_dots()
