from json import dump, load
from random import randint


class Uyelik():
    def __init__(self):
        self.calışma = True
        self.veriler = self.verileri_al()

    def verileri_al(self):
        try:
            with open("uyeler.json", "r") as dosya:
                veriler = load(dosya)
        except:
            with open("uyeler.json", "w", encoding="utf-8") as dosya:
                dosya.write("{}")
        with open("uyeler.json", "r", encoding="utf-8") as dosya:
            veriler = load(dosya)
        return veriler

    def giris_yap(self):
        while True:
            kadi = input("kullanici adini giriniz:")
            şifre = input("şifre giriniz:")
            if self.kontrol(kadi, şifre):
                print("Hoşgeldiniz")
                self.calışma = False
                break
            else:
                print("bilgiler yanlış")
                break

    def aktivasyonkodu_gonder(self, mail):
        kod = randint(100000, 999999)
        with open("{}.txt".format(mail), "w") as dosya:
            dosya.write("aktivasyon kodu:{}".format(kod))
        return kod

    def kayit_ol(self):
        kadi = input("kullanici adini giriniz:")
        şifre1 = input("şifre giriniz:")
        şifre2 = input("şifreyi tekrar giriniz:")
        while şifre1 != şifre2:
            print("şifreler uyusmuyor tekrar deneyiniz")
            şifre1 = input("şifre giriniz:")
            şifre2 = input("şifreyi tekrar giriniz:")
        mail = input("eposta giriniz:")
        if self.kayıt_varmı(kadi, mail):
            if self.aktivasyon_kontrol(mail):
                self.kayıt_et(kadi, şifre1, mail)

    def aktivasyon_kontrol(self, mail):
        aktiflik = self.aktivasyonkodu_gonder(mail)
        a = 1
        try:
            kod = int(input("aktivasyon kodu giriniz:"))
        except ValueError:
            print("lutfen sayi giriniz:")
        while aktiflik != kod:
            print("kod yanlış")
            a += 1
            try:
                kod = int(input("aktivasyon kodu giriniz:"))
            except ValueError:
                print("lutfen sayi giriniz:")
            if a > 3:
                print("aktif edilemedi daha sonra tekrar deneyiniz")
                return False
        return True

    def kayıt_varmı(self, kadi, mail):
        self.veriler = self.verileri_al()
        try:
            for kullanici in self.veriler["kullanicilar"]:
                if kullanici["kadi"] == kadi or kullanici["mail"] == mail:
                    print("mail veya kullanici adı kayıtlıdır")
                    return False
        except KeyError:
            pass
        return True

    def kayıt_et(self, kadi, şifre, mail):
        try:
            self.veriler["kullanicilar"].append({"kadi": kadi, "sifre": şifre, "mail": mail, "aktivasyon": "y"})
        except KeyError:
            self.veriler["kullanicilar"] = [{"kadi": kadi, "sifre": şifre, "mail": mail, "aktivasyon": "y"}]
        with open("uyeler.json", "w", encoding="utf-8") as dosya:
            dump(self.veriler, dosya)
            print("kayıt başarıyla oluşturuldu.")

    def kontrol(self, kadi, şifre):
        self.veriler = self.verileri_al()
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["kadi"] == kadi:
                if kullanici["sifre"] == şifre:
                    return True
                else:
                    print("şifre yanliş")
                    return False

    def şifremi_unuttum(self):
        mail = input("mail giriniz:")
        if self.mailvarmı(mail):
            if self.aktivasyon_kontrol(mail):
                ysifre = input("yeni şifre giriniz:")
                tsifre = input("tekrar giriniz:")
                while ysifre != tsifre:
                    print("şifreler uyusmuyor")
                    ysifre = input("yeni şifre giriniz:")
                    tsifre = input("tekrar giriniz:")
                self.sifredeğiştir(ysifre, mail)
        else:
            print("mail sistemde kayıtlı değil.")

    def sifredeğiştir(self, sifre, mail):
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["mail"] == mail:
                kullanici["sifre"] = sifre
                print("şifre basarıyla değiştirildi.")
                break
        with open("uyeler.json", "w") as dosya:
            dump(self.veriler, dosya)

    def menu(self):
        while True:
            try:
                secim = int(input("""
    1-Giriş yap
    2-Kayıt ol 
    3-şifremi unuttum 
    4-cıkıs

        secim:
        """))
                while secim < 1 or secim > 4:
                    print("(1-4) arasinda giriniz")
                break
            except ValueError:
                print("lutfen sayi giriniz:")
        return secim

    def mailvarmı(self, mail):
        self.veriler = self.verileri_al()
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["mail"] == mail:
                return True
        return False

    def sistem(self):
        secim = self.menu()
        if secim == 1:
            self.giris_yap()
        elif secim == 2:
            self.kayit_ol()
        elif secim == 3:
            self.şifremi_unuttum()
        elif secim == 4:
            self.calışma = False
        else:
            print("hatali kodlam")


uyelik = Uyelik()
while uyelik.calışma:
    uyelik.sistem()