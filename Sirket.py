class Sirket():
    def __init__(self, ad):
        self.ad = ad
        self.calisma = True
        with open("butce.txt", "r") as dosya:
            butce = dosya.readlines()
        para = int(butce[0].split("=")[1])
        self.totalpara = para
        with open("calişanlar.txt", "r") as dosya:
            calişanlar = dosya.readlines()
        maaslar = list()
        for çalişan in calişanlar:
            maaslar.append(int(çalişan.split("-")[-1]))
        self.topmaas = sum(maaslar)
    def total(self,paraa,i):
      with open("butce.txt","r") as dosya:
         butce=dosya.readlines()
      para=int(butce[0].split("=")[1])
      if i==1:
              para+=paraa
      elif i==2:
              para-=paraa
      elif i==3:
              para=paraa
      else:
              print("hatali kodlama")
      self.totalpara = para
      with open("butce.txt","w") as dosya:
           dosya.writelines("toplam butce={}".format(para))
    def program(self):
            secim = self.menusecim()
            if secim == 1:
                self.calısanekle()
            elif secim == 2:
                self.calışancıkar()
            elif secim == 3:
                self.verilecekmaas()
            elif secim == 4:
                self.maaslarıver()
            elif secim == 5:
                self.masrafgir()
            elif secim == 6:
                self.gelirgir()
            elif secim==7:
                print("total para:{}".format(self.totalpara))
            elif secim == 8:
                self.calisma=False
            else:
                print("hatali kodlama")
    def calısanekle(self):
        id=1
        ad=input("ad giriniz")
        soyad=input("soyad giriniz")
        yas=input("yas giriniz:")
        cinsiyet=input("cinsiyet giriniz:")
        maas=input("maas giriniz:")
        with open("calişanlar.txt","r") as dosya:
            a=dosya.readlines()
        if len(a) ==0:
            id=1
        else:
            with open("calişanlar.txt","r") as dosya:
             id=int(dosya.readlines()[-1].split(")")[0])+1
        with open("calişanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
        print("kişi eklendi")
    def calışancıkar(self):
        with open("calişanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()
        gcalisan=list()
        for calisan in calisanlar:
            gcalisan.append(" ".join(calisan[:-1].split("-")[0:2]))
        for calisan in gcalisan:
            print(calisan)
        secim=int(input("(1-{}) arasinda cikarmak istedğiniz numarayıı giriniz:".format(len(gcalisan))))
        while secim<1 or secim>len(gcalisan):
            print("tekrar deneyiniz")
            secim = int(input("(1-{}) arasinda cikarmak istedğiniz numarayıı giriniz:".format(len(gcalisan))))
        calisanlar.pop(secim-1)
        sayac=1
        dcalişanlar=list()
        for calısan in calisanlar:
            dcalişanlar.append("{}){}".format(sayac,calısan.split(")")[1]))
            sayac+=1
        with open("calişanlar.txt","w") as dosya:#w ustune yazar
            dosya.writelines(dcalişanlar)
    def verilecekmaas(self):
        with open("calişanlar.txt","r") as dosya:
            calişanlar=dosya.readlines()
        maaslar=list()
        for çalişan in calişanlar:
            maaslar.append(int(çalişan.split("-")[-1]))#-1 sondaki değeri almayı sağlar
        while True:
            secim=int(input("""
       1-calışan maaslari göster
       2-toplam verilecek maaşi göster
       3-cikiş
       
       secim:     
                            """))
            if secim==1:
                gcalisan = list()
                for calisan in calişanlar:
                    gcalisan.append(" ".join(calisan[:-1].split("-")[0:2]))
                for calisan in gcalisan:
                    print(calisan)
                secim = int(input("(1-{}) arasinda maasini görmek istediğiniz kişinin numarasini giriniz:".format(len(gcalisan))))
                while secim < 1 or secim > len(gcalisan):
                    print("tekrar deneyiniz")
                print("{} maasi={}".format(gcalisan[secim-1].split(")")[1],maaslar[secim-1]))
            elif secim==2:
               print("toplam verilecek maas={}".format(sum(maaslar)))
            elif secim==3:
                break
            else:
                print("hatali kodlama")
        self.topmaas=sum(maaslar)
    def maaslarıver(self):
        while True:
            secim=int(input("""
        1-maasları ver
        2-kalan para
        3-giden para
        4-çıkıs
        
        secim:
            """))
            if secim==1:
                self.total(self.topmaas,2)
                print("maaslar verildi.")
            elif secim==2:
                print(self.totalpara)
            elif secim==3:
                print(float(self.topmaas))
            elif secim==4:
                break
            else:
                print("hatali kodlama")
    def masrafgir(self):
        while True:
            secim = int(input("""
               1-masraf gir
               2-kalan para
               3-çıkıs
               
               secim:
                   """))
            if secim == 1:
                masraf=int(input("masraf girin:"))
                self.total(masraf,2)
            elif secim == 2:
                print(self.totalpara)
            elif secim == 3:
                break
            else:
                print("hatali kodlama")
    def gelirgir(self):
        while True:
            secim = int(input("""
               1-gelir gir
               2-kalan para
               3-çıkıs
               
               secim:
                   """))
            if secim == 1:
                gelir=int(input("gelir giriniz:"))
                self.total(gelir,1)
            elif secim == 2:
                print(self.totalpara)
            elif secim == 3:
              break
            else:
                print("hatali kodlma")
    def menusecim(self):
        print("***** {} Hoşgeldiniz *****".format(self.ad))
        secim=int(input("""
    1-çalışan ekle
    2-calısan cıkar
    3-verilecek maaşı göster
    4-maasları ver
    5-masraf gir
    6-gelir gir
    7-total para 
    8-cıkıs

     seciminizi giriniz:
        """))
        while secim<0 or secim >8:
           secim=input("secimi tekrar giriniz:")
        return  secim
şirket=Sirket("Özdemir Software")
while şirket.calisma:
    şirket.program()

