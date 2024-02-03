i = 1
while i <= 12:
    print(i,".sınıf")
    i += 1



while True:
    i = input("lutfen sifre tanimlayiniz: ")
    if len(i) == 8:
        print("karakter sayisi yeterlidir")
        break
    else:
        print("karakter sayisi yetersiz")


while True:
    print("8 karakterli sifre gir")
    sifre = str(input())
    karakters = 0
    for x in sifre:
        karakters += 1
    if karakters < 8 or karakters > 8:
        print("sifreniz sekiz haneli olmalı")
    else: print("sifreniz kaydedilmiştir")
    x = str(input())
    if x == "cikis yap":
        break


while True:
    i = input("lutfen klme gir")
    print(i.upper())

