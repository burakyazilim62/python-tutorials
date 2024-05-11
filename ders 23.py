with open("bilgi.txt","a",encoding = "utf-8") as file:
    while True:
        kelime = str(input("bir kelime giriniz"))
        bosluk = "\n"
        file.write(kelime + bosluk)
        sayi = input("cikmak isterseniz 1e basiniz")
        if sayi == "1":
            break
with open("bilgi.txt","r+",encoding="utf-8") as file:
    file.write("KEREM,HULUSİ,UMUT,İSMET,BURAK,ATA,MELİH")
    file.seek(26)
    file.write("SAVAS")