class makerCenter():
    def __init__(self,isim,soyisim,yas,cinsiyet,boy,kilo):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.boy = boy
        self.kilo = kilo
    def kizerkeklisteleme(self):
        if self.cinsiyet == "kadin":
            with open("kiz.txt","r+",encoding = "utf-8") as file:
                file.write(self.isim)
        else:
            with open("erkek.txt", "r+", encoding="utf-8") as file1:
                file1.write(self.isim)
    def bilgilerigoster(self):
        print("isim",self.isim)
        print("soyisim",self.soyisim)
        print("yas", self.yas)
        print("cinsiyet", self.cinsiyet)
        print("boy", self.boy)
        print("kilo", self.kilo)
    def vucutkitleindeksi(self):
        boym = self.boy/100
        index = self.kilo/boym**2
        if index < 18.5:
            print(index,"zayıf")
        elif index < 25:
            print(index,"normal")
        elif index < 30:
            print(index,"hafif sisman")
        elif index < 35:
            print(index,"orta sisman")
        elif index < 40:
            print(index,"agir sisman")
class ogrenci(makerCenter):
    def __init__(self, bilinendiller, isim, soyisim, yas, cinsiyet, boy, kilo):
        super().__init__(isim, soyisim, yas, cinsiyet, boy, kilo)
        self.bilinendiller = bilinendiller
    def bilgilerigoster(self):
        print("isim", self.isim)
        print("soyisim", self.soyisim)
        print("yas", self.yas)
        print("cinsiyet", self.cinsiyet)
        print("boy", self.boy)
        print("kilo", self.kilo)
        print("bilinen diller", self.bilinendiller)

class yonetici(makerCenter):
    def __init__(self,maas,isim,soyisim,yas,cinsiyet,boy,kilo):
        super().__init__(isim,soyisim,yas,cinsiyet,boy,kilo)
        self.maas = maas

    def zamyap(self):
        self.maas = self.maas * 1.65
        print("zam yapildi")

    def bilgilerigoster(self):
        print("isim", self.isim)
        print("soyisim", self.soyisim)
        print("yas", self.yas)
        print("cinsiyet", self.cinsiyet)
        print("boy", self.boy)
        print("kilo", self.kilo)
        print("maas", self.maas)
class danisman(makerCenter):
    def __init__(self,maas,isim,soyisim,yas,cinsiyet,boy,kilo):
        super().__init__(isim,soyisim,yas,cinsiyet,boy,kilo)
        self.maas = maas
    def zamyap(self):
        self.maas = self.maas*1.2
        print("zam yapildi")

class ogretmen(makerCenter):
    def __init__(self, yetkialani, isim, soyisim, yas, cinsiyet, boy, kilo):
        super().__init__(isim, soyisim, yas, cinsiyet, boy, kilo)
        self.yetkialani = yetkialani
    def bilgilerigoster(self):
        print("isim", self.isim)
        print("soyisim", self.soyisim)
        print("yas", self.yas)
        print("cinsiyet", self.cinsiyet)
        print("boy", self.boy)
        print("kilo", self.kilo)
        print("yetki alanı", self.yetkialani)

seckin = yonetici(100000,"seckin","aksoy",37,"erkek",180,90)
hulusi = ogrenci("phyton","hulusi","taskiran",14,"erkek",154,46)
savas = ogretmen("phyton","savas","metinoglu",25,"erkek",175,88)
dilara = danisman(1000,"dilara","hatırlayamıyorum",19,"kadin",170,50)
savas.vucutkitleindeksi()
seckin.bilgilerigoster()
seckin.zamyap()
seckin.bilgilerigoster()
hulusi.bilgilerigoster()
savas.bilgilerigoster()