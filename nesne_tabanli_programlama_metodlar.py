class Yazer():
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

kitap1=Yazer("Olu evinden anilar",1924,"Dram",29)
kitap2=Yazer("Cocukluk",1890,"Dram",90)
kitap1.bilgilerigoster()
kitap2.satis_ekle(20)
kitap2.bilgilerigoster()


