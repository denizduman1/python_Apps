import json
import os

class Ogrenci:
    def __init__(self,ad,soyad,num):
        self.ad = ad
        self.soyad = soyad
        self.num = num

class OgrenciKayit:
    def __init__(self):
        self.ogrenciler = []
        self.oturumAcikMi = False
        self.aktifKullanici = {}
        self.loadStudent()
        
    def loadStudent(self):
        if os.path.exists("ogrenciler.json"):
            with open("ogrenciler.json","r",encoding="utf-8") as jsonFile:
                ogrenci_Json = json.load(jsonFile)
                for ogr in ogrenci_Json:
                    ogr = json.loads(ogr)
                    newOgr = Ogrenci(ogr['ad'],ogr['soyad'],ogr['num'])
                    self.ogrenciler.append(newOgr)
            print(self.ogrenciler)
    
    def register(self,ogr:Ogrenci):
        self.ogrenciler.append(ogr)
        self.savetoFile()
        print("Kayıt Oluşturuldu.")
        print("-"*50)
    
    def savetoFile(self):
        liste = []
        for i in self.ogrenciler:
            liste.append(json.dumps(i.__dict__)) # json stringe çevrilme işlemi
        with open("ogrenciler.json","w",encoding="UTF-8") as jsonFile: #utf sorunlu.
            json.dump(liste,jsonFile) # stringi json klasörüne yükleme işlemi
            
    def login(self,ad,num):
        for ogr in self.ogrenciler:
            if(ogr.ad==ad and  ogr.num==num):
                self.oturumAcikMi = True
                self.aktifKullanici = ogr
                print("Giriş Yapıldı.")
                print("-"*50)        
    
    def logout(self):
        self.oturumAcikMi = False
        self.aktifKullanici = {}
        print("Çıkış Yapıldı.")
        print("-".center(50))

    def bilgiGoster(self):
        if (self.oturumAcikMi):
            print("Kullanıcı Adı:",self.aktifKullanici.ad)
            print("-"*50)        
        else:
            print("Giriş Yapılmamış.")
            print("-"*50)        


ogrKayit = OgrenciKayit()

while True:
    print("HOŞGELDİNİZ".center(50,"-"))
    print("1-Kayıt Et")
    print("2-Giriş Yap")
    print("3-Çıkış Yap")
    print("4-Bilgilerimi Göster")
    print("5-Çıkış Yap.")
    secim = int(input("Seçim: "))
    if secim == 5 :
        break
    elif secim == 1:
        ad = input("Öğrenci Adı:")
        soyad = input("Öğrenci Soyadı:")
        number = input("Öğrenci Numarası:")
        o1 = Ogrenci(ad,soyad,number)
        ogrKayit.register(o1)
        # print(ogrKayit.ogrenciler)
    elif secim == 2:
        if (ogrKayit.oturumAcikMi==False):
            ad = input("ad:")
            num = input("num:")
            ogrKayit.login(ad,num)
        else:
            print("Açık oturum varken başka giriş yapılamaz.")
    elif secim == 3:
        ogrKayit.logout()
    elif secim == 4:
        ogrKayit.bilgiGoster()
    else: 
        print("Hatalı Seçim")  
        print("-"*50)        
