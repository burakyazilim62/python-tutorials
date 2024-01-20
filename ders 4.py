print("notunuzu giriniz")
sayi = int(input())
sayi2 = int(input())
ortalama = (sayi+sayi2)/2
print(ortalama)
if sayi >= 0 and sayi <=100 and sayi2 >= 0 and sayi2 <= 100:
    if 85<=ortalama<=100:
        print("AA")
    elif 80<=ortalama<85:
        print("AB")
    elif 70<=ortalama<80:
        print("BB")
    elif 65<=ortalama<70:
        print("BC")
    elif 60<=ortalama<65:
        print("CC")
    elif 55<=ortalama<60:
        print("CD")
else:
    print("0la 100 arasında bir sayi girin")



    print("bir sayi giriniz")
    a = int(input())
    if a % 2 == 0:
        print("sayi cifttir")
    else:
        print("sayi tektir")

sifre = "burak3"
parola = str(input())
if sifre == parola:
    print("basariyla giris yaptiniz")
else:
    print("sifre yanlis")

    sifre = "burak3"
    parola = str(input())
    if sifre == parola:
        print("basariyla giris yaptiniz")
    else:
        print("sifre yanlis, sifreyi degistirmek ister misiniz")
        cevap = str(input())
        if cevap == "evet":
            print("yeni sifreyi giriniz")
            sifre = str(input())
            print("sifre basariyla degistirildi")
        elif cevap == "hayir":
            print("tamam")