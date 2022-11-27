def hide_password():
    x = input("şifrenizi giriniz : ")
    ln = len(x)
    print("*" * ln, "şifreniz", ln, "haneli")


hide_password()
