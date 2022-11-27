def my_discount():
    x = float(input("fiyatı giriniz :"))
    y = float(input("yüzdelik indirimi giriniz : "))
    z = (x / 100) * (100 - y)
    print(z)


my_discount()
