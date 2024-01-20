fruits = ["elma","muz","üzüm"]
for x in fruits:
    print(x)



rakamlar = [0,1,2,3,4,5,6,7,8,9]
for i in rakamlar:
    if i <= 6 and i != 0:
        print(i)
    else:
        pass



rakamlar = [1,2,3,4,5,6,7,8,9,0]
toplam = 0
for i in rakamlar:
    toplam = toplam + i
print(toplam)



deneme = [1,2,3]
guvenlik = "4567"
for i in deneme:
    print("sifrenizi giriniz")
    sifre = "burak5"
    parola = str(input())
    if sifre == parola:
        print("basariyla giris yaptınız")
        break
    elif i == 3:
        print("3 kere yanlis giris yaptiniz")
        print("lutfen guvenlik kodunu giriniz")
        kod = str(input())
        if kod == guvenlik:
            yenisifre = str(input("yeni sifreyi giriniz"))
            sifre = yenisifre
            print("basariyla sifre degistirildi")
        else:
            print("guvenlik kodu yanlis")
