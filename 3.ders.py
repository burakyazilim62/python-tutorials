rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
len(rakamlar)
rakamlar.append(22)
rakamlar.remove(22)
print(rakamlar)
rakamlar.remove(3)
print(rakamlar)
print(rakamlar[3:6])
rakamlar.remove(rakamlar[5])
print(rakamlar)

x = 32
y = 24
if x < y:
    print("x sayisi y den kucuktur")
else:
    print("x y den kucuk degildir")

print("birinci sayiyi giriniz")
ilksayi = int(input(""))
print("ikinci sayiyi giriniz")
ikincisayi = int(input(""))
if ilksayi > ikincisayi:
    print("birinci sayi ikinci sayidan buyuktur")
else:
    print("birinci sayi ikinci sayidan buyuk degildir")



    print("yapmak istediginiz islemi seciniz")
    islem = str(input())
    print("ilk sayiyi giriniz")
    a = int(input())
    print("ikinci sayiyi giriniz")
    b = int(input())
    if islem == "carpma":
        print(a * b)

    if islem == "bolme":
        print(a / b)

    if islem == "toplama":
        print(a + b)

    if islem == "cıkarma":
        print(a - b)
