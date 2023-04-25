import os
import datetime
import colorama
from colorama import Fore
ogrenciler = []

#Geçici değişkene kayıt al
def ramkaydet():
        kayittarihi = datetime.datetime.now().strftime(format='%m/%d/%y') + f" Saat: {str(datetime.datetime.now().hour)}:{str(datetime.datetime.now().minute)}"


    #ogrenci listesinde diziye isim ver ve her isime değişken ata
        ogrenci = {"ad": ad.upper(), "soyad": soyad.upper(), "yas": yas, "bölüm": bölüm.upper(), "numara": numara,"cinsiyet":cinsiyet.upper(),"tarih":kayittarihi}  

        #ogrencideki bilgileri tek tek ogrenciler listesine kayıt et
        ogrenciler.append(ogrenci)
        kaydet(ogrenciler) 

#TXT dosyasına ram'de tutulan bilgilerin kayıdı için fonksiyon
def kaydet(ogrenciler):
    with open("ogrencibilgi.txt", "w") as dosya:
        for ogrenci in ogrenciler:
            dosya.write("{}, {}, {}, {}, {}, {}, {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))

#Kayıtlı olan TXT dosyasını yükelemesi için fonksiyon
def yukle():
    ogrenciler = []
    if os.path.exists("ogrencibilgi.txt"):
        with open("ogrencibilgi.txt", "r") as dosya:
            for satir in dosya:
                satir = satir.strip()
                ad, soyad, yas, bölüm, numara,cinsiyet,kayittarihi = satir.split(", ")
                ogrenci = {"ad": ad.upper(), "soyad": soyad.upper(), "yas": yas, "bölüm": bölüm.upper(), "numara": numara,"cinsiyet":cinsiyet.upper(),"tarih": kayittarihi}
                ogrenciler.append(ogrenci)
    return ogrenciler

#Tekrar işlem yapmak istiyor mu diye sor
def tekrar(): 
    devam = input(Fore.LIGHTGREEN_EX+"Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
    if devam.lower() == "e":                        
            return(True)
    elif devam.lower() == "h":
            print(Fore.RED+"Görüşmek üzere...")
            kaydet(ogrenciler)
            return(False)                  
    
#Okutulacak değeri iste ve okut    
def okutucu(deger,aranacakdeger):
    if str(deger) in ogrenci[aranacakdeger]:
        print(Fore.MAGENTA+"\nAdı: {}  \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\nKayıt Tarihi: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))
    else:
        print(Fore.RED+"Öğrenci bulunamadı veya kayıtlı değil")

#Değiştirilecek bilgiyi iste ve değiştir
def bilgiyenile(deger):                   
            ogrenci[deger] = input(Fore.YELLOW+"Yeni bilgiyi giriniz:\n-->").upper()
            while len(ogrenci[deger])<2 :
                  print(Fore.RED+f"Lütfen doğru giriniz")
                  ogrenci[deger] = input(Fore.YELLOW+"Yeni Bilgi:\n--> ").upper()
                  if deger != "ad" or deger != "soyad":
                      if not ogrenci[deger].isalpha():
                          print(Fore.RED+f"Lütfen doğru giriniz")
                          ogrenci[deger] = input(Fore.YELLOW+"Yeni Bilgi:\n--> ").upper()
            kaydet(ogrenciler)              
                      
            print(Fore.GREEN+"Başarıyla değiştirildi")
            devam = input(Fore.GREEN+"Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
            if devam.lower() == "e":                        
               return(True)
            elif devam.lower() == "h":
              print("Görüşmek üzere...")
              kaydet(ogrenciler)
              return(False)

kayittarihi = ""

#TXT dosyasındaki kayıtları geçici değişkene ver
ogrenciler = yukle()

#Önceden bölümleri belirle
bölümler = ["YAZILIM","HUKUK","MUHASEBE","MÜZIK","MATBAA","ÖGRETMENLIK","PSIKOLOGLUK","BILGISAYAR MÜHENDISLIGI"]
while True:
   
    #İşlem türünü seçtir
    islem = input(Fore.BLUE+"\nİşlem türü seçiniz:\n1)Öğrenci Kayıt\n2)Öğrenciler\n3)öğrenci Sorgu\n4)öğrenci bilgi yenile\n5)bölüm öğrencilerini listele\n6)Cinsiyete göre listele\n-->")   
    
    #Eğer işlem cinsiyete göre listele ise çalıştır
    if islem.lower() == "cinsiyete göre listele" or islem.lower() == "6":
        cinsiyet = input("Listelenecek cinsiyeti giriniz:\n-->")
        aranacakdeger = "cinsiyet"
        for ogrenci in ogrenciler:
            okutucu(cinsiyet.upper(),aranacakdeger)

        if tekrar() == True:
            continue
        else:
            break

    #Eğer işlem cinsiyete göre listele ise çalıştır
    if islem.lower() == "bölüm öğrencilerini listele" or islem.lower() == "5":
        bölüm = input("Listelenecek bölümü giriniz:\n-->")
        aranacakdeger = "bölüm"
        for ogrenci in ogrenciler:
            okutucu(bölüm.upper(),aranacakdeger)

        if tekrar() == True:
            continue
        else:
            break

    #Eğer işlem öğrenci kayıt ise çalıştır
    if islem.lower() == "öğrenci kayıt" or islem.lower() == "1":  

        #İstediğimiz Değişkenler ve değişken türü koruması
        #While not kodu ile istediğimiz değişkeni veya girişi zorunlu kılıyoruz
        ad = input(Fore.YELLOW+"\nİsim:\n--> ")
        while len(ad)<=2 or not ad.isalpha():
            print(Fore.RED+"Lütfen isim giriniz")
            ad = input(Fore.YELLOW+"İsim:\n--> ")
        
        soyad = input(Fore.YELLOW+"Soyisim:\n--> ")
        while len(ad)<=1 or soyad.isdigit():
            print(Fore.RED+"Lütfen soyisim giriniz")
            soyad = input(Fore.YELLOW+"Soyisim:\n--> ")
        

        yas = input(Fore.YELLOW+"Yaş:\n--> ")
        while not yas.isnumeric():
            print(Fore.RED+"Lütfen Sayı giriniz")
            yas = input(Fore.YELLOW+"Yaş:\n--> ")
        while int(yas)<=17:
            print(Fore.RED+"Yaş en az 18 olabilir")
            yas = input(Fore.YELLOW+"Yaş:\n--> ") 

        bölüm = input(Fore.YELLOW+"Bölüm:\n--> ").upper()
        while bölüm.upper() not in bölümler or not bölüm.isalpha():
             print(Fore.RED+"Lütfen doğru bölüm girin")
             bölüm = input(Fore.YELLOW+"Bölüm:\n--> ").upper()

        numara = input(Fore.YELLOW+"Okul Numarası:\n--> ")
        
        for j in ogrenciler:
                  if numara in j["numara"]:
                    print(Fore.RED+"Bu numara başka öğrenciye atanmış")
                    numara = input(Fore.YELLOW+"Okul Numarası:\n--> ")
                  
        while not numara.isdigit():
            print(Fore.RED+"Lütfen Sayı giriniz")
            numara = input(Fore.YELLOW+"Okul Numarası:\n--> ")

        cinsiyet = input(Fore.YELLOW+"Cinsiyeti:\n--> ")
        while not (cinsiyet.lower()=="erkek" or cinsiyet.lower()=="kadın"):
            print(Fore.RED+"Lütfen Cinsiyeti Erkek veya Kadın olarak belirleyin")
            cinsiyet = input(Fore.YELLOW+"Cinsiyeti:\n--> ")

        ramkaydet()

        if tekrar() == True:
            continue
        else:
            break

    #Eğer işlem öğrencilerse çalıştır
    elif islem.lower() == "öğrenciler" or islem.lower() == "2":                                                     

        if len(ogrenciler) != 0:
            for ogrenci in ogrenciler: 

                #ogrenciler listesindeki her değer için ogrenciyi değiştir ve str atanan değişkenleri formatla yazdır
                print(Fore.MAGENTA+"\nAdı: {} \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\nKayıt Tarihi: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))
 
        #ogrenci karakter uzunluğu 0 ise öğrenci kayıdı yoktur de
        elif len(ogrenciler) == 0:
            print(Fore.RED+"Kayıtlı Öğrenci Yok")       
        
        if tekrar() == True:
            continue
        else:
            break
        
    #eğer işlem öğrenci sorguysa çalıştır
    elif islem.lower() == "öğrenci sorgu" or islem.lower() == "3":   

        #aranan öğrencinin numarasını iste
        ara = input("Öğrencinin numarasını veya Adını giriniz:\n--> ") 
        aranacakdeger = "numara" 

        #ogrenciker karakter uzunluğu 0 ise öğrenci kayıdı yoktur de
        if len(ogrenciler) == 0:
            print("Öğrenci Kayıtlı Değil!")

        #ogrenciler listesindeki her değer için ogrenciyi değiştir
        elif len(ogrenciler) != 0:   
            for ogrenci in ogrenciler:
                okutucu(ara.upper(),aranacakdeger)
                aranacakdeger = "ad"
                okutucu(ara.upper(),aranacakdeger)
                       
        if tekrar() == True:
            continue
        else:
            break
   
    #işlem Öğrenci bilgi yenile ise çalıştır
    elif islem.lower() == "öğrenci bilgi yenile" or islem.lower() == "4" :
        if len(ogrenciler) == 0:
            print("Öğrenci Kayıtlı Değil!")
        elif len(ogrenciler) != 0:
            numara = input("Öğrencinin numarasını giriniz:\n--> ") 
            
            #kayıtlı ogrenciler llistesinden her seferinde birini al ve girilen numara ile ogrencinin içindeki numara eşit olana kadar dene  
            for ogrenci in ogrenciler:
                if numara in ogrenci["numara"]:
                    değiştir = input("Değiştirmek istediğiniz bilgiyi seçiniz:\n1)İsim\n2)Soyisim\n3)Yaş\n4)bölüm\n5)Okul Numarası\n6)Cinsiyet\n-->")
                    
                    #değiştirlimek istenen bilgiyi sor ve girilen bilgiye göre değişkeni değiştir
                    if değiştir == "isim":                    
                       bilgiyenile("ad")
                       if bilgiyenile == True:
                         continue
                       else:
                         break

                    elif değiştir == "soyisim":
                       bilgiyenile("soyad")
                       if bilgiyenile == True:
                         continue
                       else:
                         break

                    elif değiştir == "yaş":
                        bilgiyenile("yas")
                        if bilgiyenile == True:
                         continue
                        else:
                          break
                    
                    elif değiştir == "bölüm":
                        ogrenci["bölüm"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                        while ogrenci["bölüm"] not in bölümler:
                            print("Lütfen doğru bölüm girin")
                            ogrenci["bölüm"] = input("Bölüm:\n--> ").upper()
                        print("Başarıyla değiştirildi")
                        
                    elif değiştir == "okul numarası":
                        bilgiyenile("numara")

                    elif değiştir == "cinsiyet":
                        ogrenci["cinsiyet"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                        while not (cinsiyet.lower()=="erkek" or cinsiyet.lower()=="kadın"):
                            print("Lütfen Cinsiyeti Erkek veya Kadın olarak belirleyin")
                            ogrenci["cinsiyet"] = input("Cinsiyeti:\n--> ").upper()
                    else:
                        print("Yanlış işlem girildi")            
                    
        else:
            print("Öğrenci Kayıtlı Değil!")

    else:
        print("Yanlış İşlem girdiniz lütfen dikkat edin!")    
