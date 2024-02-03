def fonksiyon(*kids):
    print("en genc cocuk" + kids[2])

fonksiyon("berk","yusuf","ahmet")


def fonks(*sayi):
    sayilar = []
    sayilar.append(sayi)
    print(sayilar)
fonks(14,76,98,21,36,123,136,2)

def fon(name,surname):
    print("hoşgeldin",name,surname)



isim = input("isim girin")
soyisim = input("soyisim giriniz")
fon(name =isim,surname=soyisim)
def fonkum(**kid):
    print("his last name is" + kid["lname"])

fonkum(fname = "yasin emrah", lname = "yağız")

def ulkem(country = "turkey"):
    print("I am from" + country)

ulkem("norway")
ulkem()
05527200882
def fonki(name,phonenumber = "telefon girilmedi"):
    print(name,"ın telefon numrası",phonenumber,"budur")
fonki("burak","87967986")
