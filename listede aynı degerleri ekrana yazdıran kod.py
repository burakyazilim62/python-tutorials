list = [1,2,2,3,4,5,6,7,7,8,9,0]

for i in list:
    if list[i] == list[i+1]:
        print(list[i])
        if list[i] == i:
            print("bu sayı indexi ile aynı degerdedir")
    else:
        pass

toplam = 0
for x in range(0,100,3):
    toplam += x
print(toplam)
toplam = 0
for i in range(0,200,9):
    print(i)

    for x in range(6):
        if x == 3: break
        print(x)
    else:
        print("bitti")






adj = ["kirmizi","sari","buyuk"]
meyve = ["elma","muz","armut"]
adet = [1,2,3]
for x in adj:
    for y in meyve:
        for z in adet:
            print(x,y)



liste1 = [1,2,3,4,5,6,7,8,9,10]
liste2 = [1,2,3,4,5,6,7,8,9,10]
for x in liste1:
    print("----------")
    for y in liste2:
        print(x*y)


liste1 = [1,2,3,4,5,6,7,8,9,10]
liste2 = [1,2,3,4,5,6,7,8,9,10]
for x in liste1:
    for y in liste2:
        if x == y:
            print(x*y)