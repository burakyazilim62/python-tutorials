def selamla(isim):
    #ismi girilen kisiyi selamlar
    print("merhabalar",isim)
def toplama(sayi1,sayi2,sayi3):
    #kullanicidan alinan 3 sayinin toplamini verir
    print(sayi1+sayi2+sayi3)
def basamakbulma():
    say = float(input("sayı girin"))
    i = 1
    while True:
        if say / 10 < 1:
            break
        say = say / 10
        i += 1
    print("sayiniz",i,"basamaklıdır")
basamakbulma()
def tekcift(sayi):
    if sayi % 2 == 0:
        print("sayi çift")
    else:
        print("sayiniz tektir")
