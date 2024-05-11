file = open("bilgiler.txt","a",encoding="utf-8")
file.write("---------------------")
file.write("\n")
isim = input("isim giriniz")
bosluk = "\n"
c = "isim:"+ isim + bosluk
file.write(c)
soyisim = input("soyisim giriniz")
f = "soyisim:"+ soyisim + bosluk
file.write(f)
yas = input("yas giriniz")
i = "yas:"+ yas + bosluk
file.write(i)
telno = input("telno giriniz")
z = "telno:" + telno + bosluk
file.write(z)
file.write("---------------------")
file.close()