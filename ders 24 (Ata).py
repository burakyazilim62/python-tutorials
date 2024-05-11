with open("notlar.txt","r+",encoding = "utf-8") as file:
    for satir in file:
        liste =satir.split(",")
        isim = liste[0]
        x = int(liste[1])
        y = int(liste[2])
        z = int(liste[3])
        z = x + y+ z
        if z /3 >50:
            print(liste[0],"geçti")
        else: print(liste[0],"kaldı")