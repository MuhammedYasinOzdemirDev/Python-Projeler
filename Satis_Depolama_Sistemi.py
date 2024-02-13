from sqlite3 import *

from random import randint
class Personel():
    def __init__(self):
        self.fiyat = 4
        self.baglantı=connect("Sistem.db")
        self.imlec=self.baglantı.cursor()
        self.a = 1
        self.Bilgileri_alma()
        self.Depodurum=True
    def Satıs(self):
        while True:
            try:
                satis=int(input("satis miktari giriniz:"))
                while satis>self.totalmal:
                    satis = int(input("satis miktari giriniz:"))
                break
            except ValueError:
                print("lutfen sayi giriniz")
        self.totalmal-=satis
        self.totalpara+=self.fiyat* satis
        self.satis+=satis
    def Alıs(self):
        while True:
            try:
                alis = int(input("alıs miktari giriniz:"))
                while alis > (self.totalpara/self.fiyat):
                    alis = int(input("alıs miktari giriniz:"))
                    continue
                break
            except ValueError:
                print("lutfen sayi giriniz")
        self.totalmal+= self.alis
        self.totalpara -= self.fiyat * self.alis
        self.alis+=alis
    def Depo_menu(self):
        while True:
           try:
            secim=int(input("""
    ---------- DEPO MENUSU ----------
            
    1-mal satısı
    2-mal alısı
    3-toplam Mal miktari goster
    4-Toplam para miktari gçster
    5-cıkıs
    
       secim:       
            """))
            break
           except ValueError:
               print("lutfen sayi giriniz")
        self.Bilgileri_alma()
        if self.a>3:
            self.a=0
            self.gun+=1
        if secim == 1:
            self.Satıs()
            self.a += 1
        elif secim == 2:
            self.Alıs()
            self.a += 1
        elif secim == 3:
            print("Total Mal:{}".format(self.totalmal))
        elif secim == 4:
            print("Total Para:{}".format(self.totalpara))
        elif secim == 5:
            self.Depodurum=False
        else:
            print("hatalı kodlama")
        self.guncelleme()
    def Bilgileri_alma(self):
      try:
        self.imlec.execute("SELECT * from Depo")
        a=list()
        for i in self.imlec.fetchall()[-1]:
            a.append(i)
        self.gun=a[0]
        self.satis=a[1]
        self.alis=a[2]
        self.totalmal=a[3]
        self.totalpara=a[4]
      except:
        self.satis = 0
        self.alis = 0
        self.totalpara = 100000
        self.totalmal = 10000
        self.gun = 1
        self.imlec.execute(
            "INSERT INTO Depo VALUES({},{},{},{},{})".format(self.gun, self.satis, self.alis, self.totalmal,self.totalpara))
      self.baglantı.commit()
    def guncelleme(self):
            if self.a == 0:
                self.satis = 0
                self.alis = 0
                self.imlec.execute(
                    "INSERT INTO Depo VALUES({},{},{},{},{})".format(self.gun, self.satis, self.alis, self.totalmal,self.totalpara))
            else:
             self.imlec.execute(
                "UPDATE Depo SET Satis_Miktari={},Giren_MAl={},Total_Mal={},Total_Para={} WHERE Gün == {}".format(self.satis, self.alis, self.totalmal, self.totalpara,self.gun))
            self.baglantı.commit()
class Sistem():
       def __init__(self,ad):
           self.ad=ad
           self.sistemdurum=True
           self.baglantı=connect("Sistem.db")
           self.imlec=self.baglantı.cursor()
           self.imlec.execute("CREATE TABLE IF NOT EXISTS Sistem(Ad TEXT,Soyad TEXT,Sifre TEXT,Mail TEXT,Mevki TEXT)")
           self.imlec.execute("CREATE TABLE IF NOT EXISTS Calısanlar(Ad TEXT,Soyad TEXT,Yas INT,Maaş INT,Mail TEXT)")
           self.imlec.execute("CREATE TABLE IF NOT EXISTS Depo(Gün INT,Satis_Miktari INT,Giren_MAl INT,Total_Mal INT,Total_Para INT)")
           self.baglantı.commit()
       def Giris_Yap(self):
        self.baglantı.commit()
        self.imlec.execute("SELECT * from Sistem")
        if len(self.imlec.fetchall())==0:
            print("Sistemde uye yoktur.")
        else:
          a=1
          eposta=input("eposta:")
          sifre=input("şifre:")
          self.imlec.execute("SELECT * from Sistem")
          for kullanici in self.imlec.fetchall():
              if kullanici[3] == eposta:
                  if kullanici[2]==sifre:
                     print("{} {} Hoşgeldiniz".format(kullanici[0],kullanici[1]))
                     a=0
                     self.Sistem_girisi(kullanici[4])
                     break
          if a!=0:
              print("Bilgiler yanlış tekrar deneyiniz.")
       def Sistem_girisi(self,mevki):
           if mevki=="Personel":
               personel=Personel()
               while personel.Depodurum:
                   personel.Depo_menu()
           else:
               yonetici=Yonetici()
               while yonetici.Ydurum:
                   yonetici.menu()
       def Kayıt_ol(self):
         ad = input("Ad giriniz:").lower().capitalize().strip()
         soyad = input("Soyad giriniz:").lower().capitalize().strip()
         mail = input("Mail giriniz:").strip()
         print(mail)
         while True:
          sec=input("""
       1-Yonetici kaydi
       2-Personel Kaydi
       
          secim:  
         """)
          if sec=="1":
              c=1
              break
          elif sec =="2":
              c=2
              break
          else:
              print("hatali kodlama")
         if self.Sisteme_kontrol(ad,soyad,mail) or c==1:
           while True:
               sifre = input("Şifre giriniz:")
               sifret = input("Şifreyi tekrar giriniz:")
               if sifre == sifret:
                   break
               print("şifreler uyuşmuyor tekrar deneyiniz")
           if c==1:
                mevki="Yönetici"
           elif c==2:
                mevki="Personel"
           self.imlec.execute("INSERT INTO Sistem VALUES('{}','{}','{}','{}','{}')".format(ad,soyad,sifre,mail,mevki))
           print("Kullanıcı başarıyla yuklenmiştir.")
         else:
             print("Sistemde kaydınız yok")
         self.baglantı.commit()
       def sifremi_unuttum(self):
        self.imlec.execute("SELECT Mail from Sistem")
        if len(self.imlec.fetchall()) == 0:
                print("Sistemde uye yoktur.")
        else:
            self.imlec.execute("SELECT Mail from Sistem")
            b = 0
            mail=input("mail giriniz:")
            for kullanici in self.imlec.fetchall():
                if kullanici[0] == mail:
                   b=1
            if b==1:
                if self.Aktivasyon_kontrol(mail):
                   while True:
                    ysifre=input("Yeni şifre giriniz:")
                    tsifre=input("Şifreyi tekrar giriniz:")
                    if ysifre==tsifre:
                        self.imlec.execute("UPDATE Sistem SET Sifre='{}' WHERE Mail=='{}'".format(ysifre,mail))
                        print("Başarıyla şifre değiştirildi.")
                        self.baglantı.commit()
                        break
                    else:
                        print("şifreler uyusmuyor tekra deneyiniz.")
            else:
                print("Sistemde mail kayıtlı değildir.")
       def aktivasyon_kodu_gonder(self,mail):
           kod=randint(100000,999999)
           with open("{}.txt".format(mail),"w") as eposta:
               eposta.write("Aktivasyon kodu:{}".format(kod))
           return kod
       def Aktivasyon_kontrol(self,mail):
           kod=self.aktivasyon_kodu_gonder(mail)
           a = 3
           while True:
              try:
               akod=int(input("Aktivasyon kodu giriniz:"))
              except ValueError:
                  print("lutfen sayi giriniz:\n{} hakkınız kaldı".format(a))
                  a-=1
                  continue
              if akod == kod:
                  return True
              elif a==1:
                  print("maalesef bilemediniz dha sonra tekrar deneyiniz.")
                  return False
              else:
                  print("yanlış girdiniz {} hakkınız kaldı".format(a))
                  a-=1
       def Sistem_Menu(self):
           while True:
              try:
               secim=int(input("""
       ---------- {} SISTEMINE HOŞGELDİNİZ ----------
       
       1-Giriş yap
       2-Kayıt ol
       3-Şifremi unuttum
       4-Çıkış
       
          secim:        
               """.format(self.ad)))
               break
              except ValueError:
                  print("lütfen sayi giriniz")
           if secim == 1:
               self.Giris_Yap()
           elif secim == 2:
               self.Kayıt_ol()
           elif secim == 3:
               self.sifremi_unuttum()
           elif secim == 4:
               self.sistemdurum=False
           else:
               print("hatali kodlama")
           self.baglantı.commit()
       def Sisteme_kontrol(self,ad,soyad,mail):
           self.baglantı.commit()
           self.imlec.execute("SELECT Ad,Soyad,Mail from Calısanlar")
           a=self.imlec.fetchall()
           print(a)
           for kullanici in a:
               if ad==kullanici[0] and soyad==kullanici[1] and mail ==kullanici[2]:
                   return True
           return False
class Yonetici():
    def __init__(self):
        self.Ydurum=True
        with connect("Sistem.db") as self.baglantı:
            self.imlec=self.baglantı.cursor()

        self.baglantı.commit()
    def menu(self):
      while True:
       try:
        secim=int(input("""
    ---------- YONETICI MENUSU ---------
    
    1-Maaşlar Menusu
    2-Çalışanlar Menusu
    3-Butce Menusu
    4-Çıkıs
    
       Secim:
        """))
        break
       except ValueError:
           print("lütfen sayi giriniz:")
      if secim == 1:
        self.maaslar_menusu()
      elif secim ==2:
          while True:
              sec = input("""
               1-Çalışan ekle
               2-Çalışan çıkar
               3-Çalışan Bilgilerini göster
               4-Çıkıs

                 Secim:    
                   """)
              if sec == "1":
                  self.calısan_ekle()
              elif sec == "2":
                  self.calısan_cıkar()
              elif sec == "3":
                  self.imlec.execute("SELECT * from Calısanlar")
                  a=self.imlec.fetchall()
                  for c,i in enumerate(a,1):
                      print("""
                      {})
                         Ad:{}
                         Soyad:{}
                         Yaş:{}
                         Maaş:{}
                         Mail:{}
                      """.format(c,i[0],i[1],i[2],i[3],i[4]))
              elif sec == "4":
                  break
              else:
                  print("hatali kodlama")
              self.baglantı.commit()
      elif secim == 3:
         self.butce_menusu()
      elif secim == 4:
          self.Ydurum=False
      else:
          print("hatali kodlama")
    def calısan_ekle(self):
        ad=input("Ad giriniz:").lower().capitalize().strip()
        soyad=input("Soyad giriniz:").lower().capitalize().strip()
        while True:
            try:
                yas=int(input("Yaş giriniz:"))
                break
            except ValueError:
                print("lütfen sayi giriniz.")
        while True:
            try:
                maas = int(input("Maas giriniz:"))
                break
            except ValueError:
                print("lütfen sayi giriniz.")
        mail=input("Mail giriniz:").strip()
        self.imlec.execute("INSERT INTO Calısanlar VALUES('{}','{}',{},{},'{}')".format(ad,soyad,yas,maas,mail))
        print("Çalışan başarıyla eklenmiştir")
    def calısan_cıkar(self):
       self.imlec.execute("SELECT Ad,Soyad,Mail from Calısanlar")
       a=self.imlec.fetchall()
       for i,kullanici in enumerate(a,1):
           print("{}){} {}".format(i,kullanici[0],kullanici[1]))
       while True:
           try:
               sec=int(input("Çıkarmak istediğiniz kişinin numarasini giriniz(1-{}):".format(len(a))))
               if sec<0 or sec>len(a):
                   print("(1-{}) arasinda sayi giriniz.".format(len(a)))
               else:
                   break
           except ValueError:
               print("lütfen sayi giriniz.")
       mail=a[sec-1][2]
       self.imlec.execute("DELETE from Calısanlar WHERE Mail=='{}'".format(mail))
       self.imlec.execute("DELETE from Sistem WHERE Mail=='{}'".format(mail))
       self.baglantı.commit()
       print("çalışan başarıyla çıkarıldı.")
    def maaslar_menusu(self):
        self.baglantı.commit()
        self.imlec.execute("SELECT Ad,Soyad,Maaş from Calısanlar")
        a=self.imlec.fetchall()
        while True:
         sec = input("""
         1-Çalışan maasları göster
         2-Toplam verilecek maaşı göster
         3-maaslari ver
         4-Çıkıs

           secim:    
             """)
         if sec=="1":
            for i,calısan in enumerate(a,1):
                print("{}){} {}:{}".format(i,calısan[0],calısan[1],calısan[2]))

         elif sec=="2":
            toplam=0
            for i in a:
                toplam+=i[2]
            print("Toplam verilecek maas:{}".format(toplam))
         elif sec =="3":
            toplam = 0
            for i in a:
                toplam += i[2]
            self.imlec.execute("SELECT Total_Para,Gün from Depo")
            a=self.imlec.fetchall()[-1]
            totalpara=a[0]
            gun=a[1]
            totalpara-=toplam
            self.imlec.execute("UPDATE Depo SET Total_Para={} WHERE Gün=={}".format(totalpara,gun))
            self.baglantı.commit()
         elif sec=="4":
             break
         else:
          print("hatali kodlama")
    def butce_menusu(self):
        self.baglantı.commit()
        self.imlec.execute("SELECT Total_Para,Gün from Depo")
        a = self.imlec.fetchall()[-1]
        while True:
            sec = input("""
            1-Total para
            2-Gelir gir
            3-Masraf gir
            4-Çıkıs

              secim:    
                """)
            if sec == "1":
               print("Total Para:{}".format(a[0]))
            elif sec == "2":
                while True:
                    try:
                        gelir=int(input("Gelir giriniz:"))
                        break
                    except ValueError:
                        print("lütfen sayi giriniz.")
                tpara=a[0]
                tpara+=gelir
                gun=a[1]
                self.imlec.execute("UPDATE Depo SET Total_Para={} WHERE Gün=={}".format(tpara, gun))
            elif sec == "3":
                while True:
                    try:
                        masraf = int(input("Masraf giriniz:"))
                        break
                    except ValueError:
                        print("lütfen sayi giriniz.")
                tpara = a[0]
                tpara -= masraf
                gun = a[1]
                self.imlec.execute("UPDATE Depo SET Total_Para={} WHERE Gün=={}".format(tpara, gun))
            elif sec == "4":
                break
            else:
                print("hatali kodlama")
            self.baglantı.commit()
sistem=Sistem("OZDEMIR")
while sistem.sistemdurum:
    sistem.Sistem_Menu()
