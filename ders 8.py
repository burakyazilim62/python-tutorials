i = 2
while i<6:
    print(i)
    i += 1


i = 1
while i < 6:
    print(i)
    if i ==3:
        break
    i += 1


  toplam = 1
i = 1
while toplam<102:
    i +=1
    i += toplam
    print(i,toplam)
print(i,"inci satirda",toplam,"sayisi ile 102 yi gecmistir")

i = 0
while i < 6:
    i +=1
    if i ==3:
        continue
    print(i)

    sayi = 1
    while sayi < 100:
        if sayi % 2 != 0:
            print(sayi)
        sayi += 1
