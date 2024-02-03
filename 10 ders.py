meyve = ["kivi","muz","kiraz","mango","elma","armut"]
newlist = []
newlist2 = []
for x in meyve:
    if "a" in x:
        newlist.append(x)
    else:
        newlist2.append(x)
print(newlist)
print(newlist2)

i = 0
ikilist = []
uclist = []
dortlist = []
beslist = []
while i <= 100:
    if i % 2 == 0:
        ikilist.append(i)
    if i % 3 == 0:
        uclist.append(i)
    if i % 4 == 0:
        dortlist.append(i)
    if i % 5 == 0:
        beslist.append(i)
    i += 1
print(ikilist)
print(uclist)
print(dortlist)
print(beslist)

i = 0
toplam = 0
while i < 101:
    if i % 2 != 0:
        toplam = i + toplam
    i += 1
print(toplam)

sayilar = []
for x in range(5):
    sayi = int(input())
    sayilar.append(sayi)
print(sayilar)