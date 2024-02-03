while True:
    secim = int(input("yapmak istediginiz secimin numarasını giriniz"))
    print("1.asal kontorl")
    print("2.çıkış")
    a = int(input("lutfen sayi giriniz"))
    i = 2
    while i < a:
        if a % i == 0:
            print("bu sayi asal degildir")
            break
        i +=1
    else:
        print("bu sayi asaldır")


a = 0
while True:
    if a < 10:
        a += 1
        print(a)
    else:
        print("10a vardık")
        break

        for sayi in range(2, 101):
            asal = True
            for i in range(2, int(sayi ** 0.5) + 1):
                if sayi % i == 0:
                    asal = False
                    break
            if asal:
                print(sayi, end=" ")


