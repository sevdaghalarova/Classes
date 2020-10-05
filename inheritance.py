class Kitap():
    def __init__(self,kitap,yil,tur,satis_miktari):
        self.kitap=kitap
        self.yil=yil
        self.tur=tur
        self.satis_miktari=satis_miktari
    def bilgilerigoster(self):
        print("""
        Kitap: {}
        Yil  : {}
        Tur  : {}
        Satis miktari : {}
        """.format(self.kitap,self.yil,self.tur,self.satis_miktari))
    def satis_ekle(self,satis):
        print("Bilgiler guncelleniyor....")
        self.satis_miktari+=satis

# overriding ve super islemleri
class Yazar(Kitap):
    def __init__(self,kitap,yil,tur,satis_miktari,yazar):
        super().__init__(kitap,yil,tur,satis_miktari)
        self.yazar=yazar
    def yazar_degis(self,yeni_yazar):
        self.yazar=yeni_yazar

    def bilgileri_goster(self):
        print("""
        Kitap: {}
        Yil  : {}
        Tur  : {}
        Satis miktari : {}
        Yazar: {}
        """.format(self.kitap, self.yil, self.tur, self.satis_miktari,self.yazar))


kitap=Yazar("Cocukluk",1990,"dram",4,"Maksim Gorki")

kitap.yazar_degis("Maksim")
kitap.bilgileri_goster()
