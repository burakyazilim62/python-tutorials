with open("futbolcular2.txt","r",encoding = "utf-8") as file:
    gs = []
    fb = []
    bjk = []
    for satir in file:
        deger = satir.split(",")
        print(satir)
        if deger[1] == "Galatasaray\n":
            gs.append(satir)
        elif deger[1] == "Fenerbahce\n":
            fb.append(satir)
        else:
            bjk.append(satir)
    with open("gs2.txt","w",encoding = "utf-8") as file2:
        for i in gs:
            file2.write(i)
    with open("fb2.txt", "w", encoding="utf-8") as file3:
        for i in fb:
            file3.write(i)
    with open("bjk2.txt", "w", encoding="utf-8") as file4:
        for i in bjk:
            file4.write(i)

with open("notlar.txt","r",encoding= "utf-8") as file:
    for satir in file:
        deger = satir.split(",")
        vize = int(deger[1])
        final = int(deger[2])
        odev = int(deger[3])
        isim = deger[0]
        ortalama = vize*0.2 + final*0.5 + odev*0.3
        if ortalama > 50:
            print(isim,ortalama,"ortalama yaparak dersten gecmistir")
        else:
            print(isim,ortalama,"ortalama yaparak dersten kalmistir")
