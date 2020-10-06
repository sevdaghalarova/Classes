class Kumanda():
    def __init__(self,durum="Acik",ses=0,kanal_listesi=["TRT"],suanki_kanal="TRT"):
        self.durum=durum
        self.ses=ses
        self.kanal_listesi=kanal_listesi
        self.suanki_kanal=suanki_kanal
    def __str__(self):
        return "Durum: {}\nSes: {}\nKanallar: {}\nIzledigin Kanal: {}".format(self.durum,self.ses,self.kanal_listesi,self.suanki_kanal)
    def Ac(self):
        if self.durum=="Acik":
            print("Televizyon zaten Acik..")
        else:
            print("Televizyon aciliyor...")
            self.durum="Acik"
    def Kapat(self):
        if self.durum=="Kapali":
            print("Televizyon zaten kapali...")
        else:
            print("Televizyon kapaniyor...")
            self.durum="Kapali"
    def ses_artir(self):
        if self.ses!=32:
            self.ses+=1
            print("Sesi artirdiniz",self.ses)
    def ses_azalt(self):
        if self.ses!=0:
            self.ses-=1
            print("Sesi Azaltdiniz",self.ses)
    def kanal_ekle(self,yenikanal):
        self.kanal_listesi.append(yenikanal)
        return self.kanal_listesi


kumanda=Kumanda()

while True:
   print("""
Islem Secin
1. Tv Bilgileri
2. Tv Ac
3. Tv Kapat
4. Ses Artir
5. Ses Azalt
6. Kanal Ekle
   Cikis icin "q"-e basin
 """)
   islem=input("Islem secin: ")
   if islem=="q":
       break
   elif islem=="1":
       print(kumanda)
   elif islem=="2":
       kumanda.Ac()
   elif islem=="3":
       kumanda.Kapat()
   elif islem=="4":
       kumanda.ses_artir()
   elif islem=="5":
       kumanda.ses_azalt()
   elif islem=="6":
       yeni_kanal=input("Hangi kanali eklemek istersin? ")
       kumanda.kanal_ekle(yeni_kanal)
   else:
       print("Gecersiz islem.. ")






