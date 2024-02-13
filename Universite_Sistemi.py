from sqlite3 import *
class Universite():
    def __init__(self):
        with connect("UNIVERSİTE.db") as self.baglanti:
            self.imlec=self.baglanti.cursor()
            self.imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler(İsim TEXT,Soyad TEXT,Fakulte TEXT,Bolum TEXT,Numara INT,Ögrenim_Türü TEXT,Durum TEXT)")
            self.baglanti.commit()
        self.calisma=True
    def secim(self):
        while True:
         try:
          secim=int(input("""
    1-Öğrenci kaydi
    2-Öğrencileri görüntüleme
    3-Öğrencileri silme
    4-Öğrencileri düzenleme
    5-Çıkış
    
       seçim(1-5):            
          """))
          break
         except ValueError:
             print("lutfen sayi giriniz")
        return secim
    def sistem(self):
        sec=self.secim()
        if sec == 1:
            self.ogrenci_kaydi()
        elif sec == 2:
            self.ogrencileri_goruntuleme()
        elif sec == 3:
            self.ogrenci_silme()
        elif sec == 4:
            self.ogrenci_duzenleme()
        elif sec == 5:
            self.baglanti.commit()
            self.baglanti.close()
            self.calisma=False
        else:
            print("hatali sayi girişi lütfen tekrar deneyiniz.")
    def ogrenci_kaydi(self):
        isim=input("isim giriniz:").lower().capitalize()
        soyad=input("soyad giriniz:").lower().capitalize()
        fakulte=input("fakulte giriniz:").lower().capitalize()
        bolum=input("bolum giriniz:").lower().capitalize()
        while True:
            try:
                numara=int(input("numara giriniz:"))
                break
            except ValueError:
                print("lutfen sayi giriniz:")
        ogrenim_turu=input("ogrenim turu giriniz:").lower().capitalize()
        durum="Aktif"
        self.imlec.execute("INSERT INTO ogrenciler VALUES('{}','{}','{}','{}',{},'{}','{}')".format(isim,soyad,fakulte,bolum,numara,ogrenim_turu,durum))
        self.baglanti.commit()
    def ogrencileri_goruntuleme(self):
        self.imlec.execute("SELECT * from ogrenciler")
        s=1
        for isim,soyad,fakulte,bolum,numara,öğrenimt,durum in self.imlec.fetchall():
            print("""
    {})
       İsim: {}
       Soyad: {}
       Fakulte: {}
       Bolum: {}
       Numara: {}
       Ögrenim türü: {}
       Durum: {}
            """.format(s,isim,soyad,fakulte,bolum,numara,öğrenimt,durum))
            s+=1
    def ogrenci_silme(self):
        self.baglanti.commit()
        self.imlec.execute("SELECT İsim,Soyad,Numara from ogrenciler")
        s=1
        for isim,soyad,numara in self.imlec.fetchall():
            print("{}-{} {} no:{}".format(s,isim,soyad,numara))
            s+=1
        while True:
            try:
                no=int(input("cıkarmak istediğiniz kisiniz no sunu giriniz:"))
                a=0
                self.imlec.execute("SELECT Numara from ogrenciler")
                for num in self.imlec.fetchall():
                    if num[0]==no:
                        a=1
                if a==1:
                    break
                print("lutfen doğru numara giriniz:")
            except ValueError:
                print("lutfen sayi giriniz:")
        self.imlec.execute("DELETE  from ogrenciler WHERE Numara=={}".format(no))
        print("öğrenci basariyla silindi.")
        self.baglanti.commit
    def ogrenci_duzenleme(self):
      self.baglanti.commit()
      while True:
         try:
          sec=int(input("""
    1-Durum değişiklik
    2-fakulte dğişikliği
    3-bolum değişikliği
    4-ogrenim turu değişikliği
    5-cıkıs
        """))
          break
         except ValueError:
            print("lutfen sayi giriniz.")
      if sec==1:
          self.imlec.execute("SELECT İsim,Soyad,Numara from ogrenciler")
          s = 1
          for isim, soyad, numara in self.imlec.fetchall():
              print("{}-{} {} no:{}".format(s, isim, soyad, numara))
              s += 1
          while True:
              try:
                  no = int(input("durumunu değiştirmek istediğiniz kisiniz no sunu giriniz:"))
                  a = 0
                  self.imlec.execute("SELECT Numara,Durum from ogrenciler")
                  for num in self.imlec.fetchall():
                      if num[0] == no:
                          a = 1
                          durum=num[1]
                  if a == 1:
                      break
                  print("lutfen doğru numara giriniz:")
              except ValueError:
                  print("lutfen sayi giriniz:")
          if durum=="Aktif":
            durum="PASİF"
          else:
              durum="Aktif"
          self.imlec.execute("UPDATE ogrenciler SET Durum='{}' WHERE Numara == {}".format(durum,no))
          print("durum basarıyla değiştirildi")
      elif sec==2:
          self.imlec.execute("SELECT İsim,Soyad,Numara from ogrenciler")
          s = 1
          for isim, soyad, numara in self.imlec.fetchall():
              print("{}-{} {} no:{}".format(s, isim, soyad, numara))
              s += 1
          while True:
              try:
                  no = int(input("fakultesini değiştirmek istediğiniz kisiniz no sunu giriniz:"))
                  a = 0
                  self.imlec.execute("SELECT Numara,Fakulte from ogrenciler")
                  for num in self.imlec.fetchall():
                      if num[0] == no:
                          a = 1
                  if a == 1:
                      break
                  print("lutfen doğru numara giriniz:")
              except ValueError:
                  print("lutfen sayi giriniz:")
          fakulte=input("fakulte giriniz:").lower().capitalize()
          self.imlec.execute("UPDATE ogrenciler SET Fakulte='{}' WHERE Numara=={}".format(fakulte,no))
          pass
      elif sec==3:
          self.imlec.execute("SELECT İsim,Soyad,Numara from ogrenciler")
          s = 1
          for isim, soyad, numara in self.imlec.fetchall():
              print("{}-{} {} no:{}".format(s, isim, soyad, numara))
              s += 1
          while True:
              try:
                  no = int(input("Bolumunu değiştirmek istediğiniz kisiniz no sunu giriniz:"))
                  a = 0
                  self.imlec.execute("SELECT Numara,Bolum from ogrenciler")
                  for num in self.imlec.fetchall():
                      if num[0] == no:
                          a = 1
                          durum = num[1]
                  if a == 1:
                      break
                  print("lutfen doğru numara giriniz:")
              except ValueError:
                  print("lutfen sayi giriniz:")
          bolum=input("bolum giriniz").lower().capitalize()
          self.imlec.execute("UPDATE ogrenciler SET Bolum='{}' WHERE Numara == {}".format(bolum,no))
      elif sec == 4:
          pass
      self.baglanti.commit()
marmara=Universite()
while marmara.calisma:
    marmara.sistem()


