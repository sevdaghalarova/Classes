class Kitap():
    def __init__(self,kitap,yil,tur,satis_miktari):
        self.kitap=kitap
        self.yil=yil
        self.tur=tur
        self.satis_miktari=satis_miktari

    def __str__(self):
        return "Kitap Ismi:{}\nYil {}\nTur: {}\nSatis Miktari: {}".format(self.kitap,self.yil,self.tur,self.satis_miktari)
    def __len__(self):
        return self.satis_miktari

    def __del__(self):
        print("Obje siliniyorr..")

kitap=Kitap("Ask",2010,"Felsefi",500)
print(kitap)
len(kitap)
del kitap



