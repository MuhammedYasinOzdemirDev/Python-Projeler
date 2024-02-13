from random import choice
class Mp3calar():
    def __init__(self,sarkilar=list()):
        self.sarkilar=sarkilar
        self.calışma=True
        self.ses=100
        self.suancalansarki=str()
    def menu(self):
        secim=int(input("""
  sarki listesi:{}
  suan calan sarki:{}
  ses:{}
    1-sarkı sec
    2-ses arttır
    3-ses azalt    
    4-rasgele sarki şeç
    5-sarkı ekle
    6-sarkı sil
    7-sarkıları goster
    8-kapat
      
      secim:    
        """.format(self.sarkilar,self.suancalansarki,self.ses)))
        return secim
    def ses_arttir(self):
        while True:
            sesarttirmamiktari=int(input("ses arttirma miktarini giriniz:"))
            if (sesarttirmamiktari+self.ses)<=100:
                self.ses+=sesarttirmamiktari
                break
            else:
                print("fazla ses artırma miktari tekrar deneyiniz")
        print("ses miktari:{}".format(self.ses))
    def ses_azalt(self):
       while True:
         sesazaltmamiktari = int(input("ses azaltma miktarini giriniz:"))
         if (self.ses-sesazaltmamiktari)>=0:
            self.ses -= sesazaltmamiktari
            break
         else:
            print("fazla ses azaltma miktari tekrar deneyiniz")
       print("ses miktari:{}".format(self.ses))
    def rasgele_sarki(self):
        rasgelesarki=choice(self.sarkilar)
        self.suancalansarki=rasgelesarki
        print("{} sarkisi calınıyor".format(rasgelesarki))
        return rasgelesarki
    def sarki_ekle(self):
        sarki=input("eklemek istediğiniz sarkiyi giriniz:")
        sanatci=input("sanatcısını giriniz:")
        self.sarkilar.append(sarki)
        print("sarki eklendi.")
    def sarki_sil(self):
        for sarki in range(len(self.sarkilar)):
            print("{}-{}".format(sarki+1,self.sarkilar[sarki]))
        şarki=int(input("(1-{}) arasi cıkarmak istediğinz sarki numarasini giriniz:".format(len(self.sarkilar))))
        self.sarkilar.pop(sarki-1)
        print("sarki çıkarıldı")
    def program(self):
        i=self.menu()
        if i==1:
            self.sarkısec()
        elif i==2:
            self.ses_arttir()
        elif i==3:
            self.ses_azalt()
        elif i==4:
            self.rasgele_sarki()
        elif i==5:
            self.sarki_ekle()
        elif i==6:
            self.sarki_sil()
        elif i==7:
            for sarki in range(len(self.sarkilar)):
                print("{}-{}".format(sarki + 1, self.sarkilar[sarki]))
        elif i==8:
            self.calışma=False
        else:
            print("hatali kodlama")
    def sarkısec(self):
        for sarki in range(len(self.sarkilar)):
            print("{}-{}".format(sarki + 1, self.sarkilar[sarki]))
        secim = int(input("(1-{}) arasi şecim yapınız".format(len(self.sarkilar))))
        while secim < 0 or secim > len(self.sarkilar):
            secim = int(input("tekrar deneyiniz:"))
        print("{} sarkısı calınıyor".format(self.sarkilar[secim - 1]))
        self.suancalansarki=self.sarkilar[secim-1]
şarkilar=list()
mp3=Mp3calar(şarkilar)
while mp3.calışma:
        mp3.program()