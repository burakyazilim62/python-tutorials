class yazilimci():
    def __init__(self,isim,maas,bildigidiller,rutbe,yas):
        self.isim = isim
        self.maas = maas
        self.bildigidiller = bildigidiller
        self.rutbe = rutbe
        self.yas = yas
    def zamyap(self):
        self.maas = self.maas*1.2
    def bilgigoster(self):
        print(self.isim, self.maas, self.bildigidiller, self.rutbe,self.yas)
    def rutdeg(self):
        self.rutbe = input("yeni rutbe giriniz")


yazilimci1 = yazilimci(isim="savas",maas=17002,bildigidiller=["c+","java","phyton"],rutbe="junior",yas=28)

yazilimci.zamyap(yazilimci1)
yazilimci1.bilgigoster()
yazilimci1.rutdeg()
yazilimci1.bilgigoster()
class calisan():
    def __init__(self,isim,maas,rutbe):
        self.isim = isim
        self.maas = maas
        self.rutbe = rutbe
class yonetici(calisan):
    pass
class guvenlik(calisan):
    pass
class veznedar(calisan):
    pass
hulusi = yonetici(isim="hulusi",maas=100000,rutbe=yonetici)
umut = veznedar(isim="umut",maas=30000,rutbe=veznedar)
ata = guvenlik(isim="ata",maas=60000,rutbe=guvenlik)
