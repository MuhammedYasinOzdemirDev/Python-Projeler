class Ucus():
    def __init__(self,kod,yolcu,kapasite,kalkiş,variş,sure):
        self.kod=kod
        self.yolcu=yolcu
        self.kapasite=kapasite
        self.kalkis=kalkiş
        self.variş=variş
        self.sure=sure
        print("{} numarali ucak eklendi".format(self.kod))
    def Menu(self):
         return int(input( """
           1-anons yap
           2-bilet satiş 
           3-bilet iptal
           4-mevcut durum
           5-cıkıs
            
             secim:
           """))
    def anonsyap(self):
        print("{} kod numarali ucak {}-{} arasi {} dakika sürecektir".format(self.kod,self.kalkis,self.variş,self.sure))
    def biletsatis(self,bilet=1):
           koltuksayisi=self.kapasite-self.yolcu
           if bilet<=koltuksayisi:
               koltuksayisi-=bilet
               self.yolcu+=bilet
           else:
               print("yetersiz kapasite")
    def biletiptal(self,bilet=1):
        koltuksayisi=self.kapasite-self.yolcu
        if bilet <= self.yolcu:
            koltuksayisi += bilet
            self.yolcu-=bilet
        else:
            print("fazla kapasite")
    def mevcutdurum(self):
        kalan=self.kapasite-self.yolcu
        print("""
         {} kod numarali {}-{} seferini yapan ucakta {} yolcu vardir
         {} bilet satilmis kalan koltuk sayisi {} dir
        """.format(self.kod,self.kalkis,self.variş,self.yolcu,self.yolcu,kalan))
def ucaklarr():
    for i in range(len(ucaklar)):
        print("{}-{} kod numarali {}-{} seferi yapan ucak".format(i+1,ucaklar[i].kod,ucaklar[i].kalkis,ucaklar[i].variş))
def ucaklarmenusu():
         return int(input("""
              1-ucak ekle
              2-ucak cıkar
              3-ucak durumu goster
              4-ucakları goster
              5-cıkıs        
              secim:
            """))
durum=True
ucaklar = list()
while durum:
    secim=ucaklarmenusu()
    if secim == 1:
        kod=input("ucak kodu giriniz:")
        yolcu=int(input("yolcu sayisini giriniz:"))
        kapasite=int(input("ucak kapasitesini giriniz:"))
        while yolcu>kapasite:
            print("hatali kodlama tekrar deneyiniz")
            yolcu = int(input("yolcu sayisini giriniz:"))
            kapasite = int(input("ucak kapasitesini giriniz:"))
        kalkis=input("kalkiş yerini giriniz:")
        variş=input("variş yerini giriniz:")
        sure=input("gecen sureyi giriniz:")
        ucaklar.append(Ucus(kod,yolcu,kapasite,kalkis,variş,sure))
    elif secim == 2:
        ucaklarr()
        cıkar=int(input("cıkarmak istediğiniz ucağin numarasini giriniz"))
        ucaklar.pop(cıkar-1)
    elif secim == 3:
        ucaklarr()
        if len(ucaklar)!=0:
         ucak=int(input("durumunu ogrenmek istediğiniz ucagın numarasini giriniz:"))
         while ucak<0 or ucak>(len(ucaklar)):
             print("hatali kodlama tekrar deneyiniz:")
             ucak = int(input("durumunu ogrenmek istediğiniz ucagın numarasini giriniz:"))
         while durum:
            secim = ucaklar[ucak-1].Menu()
            if secim == 1:
               ucaklar[ucak-1].anonsyap()
            elif secim == 2:
              bilet = int(input("bilet sayisi giriniz:"))
              ucaklar[ucak-1].biletsatis(bilet)
            elif secim == 3:
              bilet = int(input("bilet sayisi giriniz:"))
              ucaklar[ucak-1].biletiptal(bilet)
            elif secim == 4:
               ucaklar[ucak-1].mevcutdurum()
            elif secim == 5:
               break
            else:
              print("hatali kodlama")
        else:
             print("ucak mevcut değildir.")
    elif secim == 4:
        ucaklarr()
    elif secim == 5:
        break
    else:
        print("hatali kodlama")




