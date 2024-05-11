import pywhatkit

try:
    a = int(input("sayı giriniz"))
    b = int(input("sayı giriniz"))
    print(a/b)
except ValueError:
    print("deger hatasi yaptiniz")
except ZeroDivisionError:
    print("hicbir sayi 0a bolunmez")