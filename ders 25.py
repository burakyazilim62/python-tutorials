class araba():
    model = "renault megane"
    yil = 2010
    beygirgucu = 110
    renk = "gri"

araba1 = araba()
print(araba1.model,araba1.yil)
class araba():
    def __init__(self,model,yil,beygirgucu,renk,kky = "belirtilmemiş"):
        self.model = model
        self.yil = yil
        self.beygirgucu = beygirgucu
        self.renk = renk
        self.kilometrede_kac_yakar = kky
araba1 = araba(model ="renault megane",yil = 2010,beygirgucu=120,renk="kirmizi",kky= "20krs")
araba2 = araba(model ="bmv f30",yil = 2018,beygirgucu=200,renk="siyah")
print(araba1.model,"-----------",araba2.model)
print(araba1.renk,"-----------",araba2.renk)
print(araba1.yil,"-----------",araba2.yil)
print(araba1.beygirgucu,"-----------",araba2.beygirgucu)
print(araba1.kilometrede_kac_yakar,"-----------",araba2.kilometrede_kac_yakar)
