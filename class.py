# Python Nesne tabanli programlama dilidir

# Python programming object'ler ile calisiyor
# her bir object'in degisik metodlari vardir
# kendi objectimizi nasil olusturacagiz:


# Araba sinfi olusturalim
class Araba(): # class ifadesi ile sinif olusturuyoruz
    model="Porche" # arabanin modeli
    renk="kirmizi" # arabanin rengi

# simdi Araba sinfindan bir object olusturalim
araba=Araba()
# Araba sinfindan 2-ci bir araba1 object olusturalim
araba1=Araba()
print(araba.model) # araba objectinin modelini (metod) cagiriyoruz
# Goruyoruz ki iki objectin de modeli ayni sonucu veriyor. Cunki bu Araba sinfinin attribute-lari

print(araba1.model)
# bunun icin bize _init_  fonksiyonu yardimci olacaktir

# Arabalar sinfi olusturyoruz
class Arabalar():
    def __init__(self,model,renk): # init fonksiyonu olusturduk
        # self objektin kendisini ifade ediyor
         self.model=model
         self.renk=renk

# Simdi Arabalar sinfindan object olusturalim
arabalar1=Arabalar("Jeep","siyah")
arabalar2=Arabalar("Hundai","Beyaz")
print(arabalar1.model)
print(arabalar2.model)

# her iki objenin modelinin farkli gosterildigini gorecegiz

