def your_vat():
    while True:
        fyt = int(input("ürünün fiyatını giriniz : "))
        kdv = int(input("ürünün vergi oranınını giriniz : "))
        top = fyt+((fyt*kdv)/100)
        print(top)
your_vat()