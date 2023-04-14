import os
import datetime
ogrenciler = []

def kaydet(ogrenciler):
    with open("ogrencibilgi.txt", "w") as dosya:
        for ogrenci in ogrenciler:
            dosya.write("{}, {}, {}, {}, {}, {}, {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))

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




kayittarihi = ""
ogrenciler = yukle()
bölümler = ["YAZILIM","HUKUK","MUHASEBE","MÜZIK","MATBAA","ÖGRETMENLIK","PSIKOLOGLUK","BILGISAYAR MÜHENDISLIGI"]
while True:
    #İşlem türünü seçtir
    islem = input("\nİşlem türü seçiniz:\n1)Öğrenci Kayıt\n2)Öğrenciler\n3)öğrenci Sorgu\n4)öğrenci bilgi yenile\n5)bölüm öğrencilerini listele\n6)Cinsiyete göre listele\n-->")   
    
    if islem.lower() == "cinsiyete göre listele" or islem.lower() == "6":
        cinsiyet = input("Listelenecek cinsiyeti giriniz:\n-->")
        for ogrenci in ogrenciler:
            if cinsiyet.upper() in ogrenci["cinsiyet"]:
                print("\nAdı: {}  \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))

        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() == "e":                        
            continue
        elif devam.lower() == "h":
            print("Görüşmek üzere...")
            kaydet(ogrenciler)
            break




    if islem.lower() == "bölüm öğrencilerini listele" or islem.lower() == "5":
        bölüm = input("Listelenecek bölümü giriniz:\n-->")
        for ogrenci in ogrenciler:
            if bölüm.upper() in ogrenci["bölüm"]:
                print("\nAdı: {}  \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"]))

        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() == "e":                        
            continue
        elif devam.lower() == "h":
            print("Görüşmek üzere...")
            kaydet(ogrenciler)
            break        

    #Eğer işlem öğrenci kayıt ise değişkenleri girmesini iste
    if islem.lower() == "öğrenci kayıt" or islem.lower() == "1":  

        #İstediğimiz Değişkenler ve değişken türü koruması
        #While not kodu ile istediğimiz değişkeni veya girişi zorunlu kılıyoruz
        ad = input("\nİsim:\n--> ")
        while len(ad)<=2:
            print("Lütfen isim giriniz")
            ad = input("İsim:\n--> ")
        while not ad.isalpha():
            print("Lütfen isim giriniz")
            ad = input("İsim:\n--> ")

        soyad = input("Soyisim:\n--> ")
        while len(ad)<=1:
            print("Lütfen soyisim giriniz")
            soyad = input("Soyisim:\n--> ")
        while not soyad.isalpha():
            print("Lütfen soyisim giriniz")
            soyad = input("Soyisim:\n--> ")

        yas = input("Yaş:\n--> ")
        while not yas.isdigit():
            print("Lütfen Sayı giriniz")
            yas = input("Yaş:\n--> ")
        while int(yas)<=17:
            print("Yaş en az 18 olabilir")
            yas = input("Yaş:\n--> ") 

        bölüm = input("Bölüm:\n--> ").upper()
        while bölüm.upper() not in bölümler:
             print("Lütfen doğru bölüm girin")
             bölüm = input("Bölüm:\n--> ").upper()

        while not bölüm.isalpha():
            print("Lütfen bölüm giriniz")
            bölüm = input("Bölüm:\n--> ")

        numara = input("Okul Numarası:\n--> ")
        i = 0
        while int(i) < 1:
              for j in ogrenciler:
                  if numara in j["numara"]:
                    print("Bu numara başka öğrenciye atanmış")
                    numara = input("Okul Numarası:\n--> ")
                  elif numara not in j["numara"]:
                      i = 2 
        while not numara.isdigit():
            print("Lütfen Sayı giriniz")
            numara = input("Okul Numarası:\n--> ")

        cinsiyet = input("Cinsiyeti:\n--> ")
        while not (cinsiyet.lower()=="erkek" or cinsiyet.lower()=="kadın"):
            print("Lütfen Cinsiyeti Erkek veya Kadın olarak belirleyin")
            cinsiyet = input("Cinsiyeti:\n--> ")
        kayittarihi = datetime.datetime.now().strftime(format='%m/%d/%y') + f" Saat: {str(datetime.datetime.now().hour)}:{str(datetime.datetime.now().minute)}"
        #ogrenci listesinde diziye isim ver ve her isime değişken ata
        ogrenci = {"ad": ad.upper(), "soyad": soyad.upper(), "yas": yas, "bölüm": bölüm.upper(), "numara": numara,"cinsiyet":cinsiyet.upper(),"tarih":kayittarihi}  

        #ogrencideki bilgileri tek tek ogrenciler listesine kayıt et
        ogrenciler.append(ogrenci)
        kaydet(ogrenciler) 

        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() == "e":                        
            continue
        elif devam.lower() == "h":
            print("Görüşmek üzere...")
            kaydet(ogrenciler)
            break

    #Eğer işlem öğrencilerse çalıştır
    elif islem.lower() == "öğrenciler" or islem.lower() == "2":                                                     

        if len(ogrenciler) != 0:
            for ogrenci in ogrenciler: 

                #ogrenciler listesindeki her değer için ogrenciyi değiştir ve str atanan değişkenleri formatla yazdır
                print("\nAdı: {} \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\nKayıt Tarihi: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))
 
        #ogrenci karakter uzunluğu 0 ise öğrenci kayıdı yoktur de
        elif len(ogrenciler) == 0:
            print("Kayıtlı Öğrenci Yok")       
        
        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")    

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() != "e":                   
              print("Görüşmek Üzere...")
              kaydet(ogrenciler)
              break
        
    #eğer işlem öğrenci sorguysa çalıştır
    elif islem.lower() == "öğrenci sorgu" or islem.lower() == "3":   

        #aranan öğrencinin numarasını iste
        numara = input("Öğrencinin numarasını giriniz:\n--> ")  

        #ogrenciker karakter uzunluğu 0 ise öğrenci kayıdı yoktur de
        if len(ogrenciler) == 0:
            print("Öğrenci Kayıtlı Değil!")

        #ogrenciler listesindeki her değer için ogrenciyi değiştir
        elif len(ogrenciler) != 0:   
            for ogrenci in ogrenciler:
                if numara in ogrenci["numara"]:                          
                    print("\nAdı: {}  \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\nKayıt Tarihi: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"],ogrenci["tarih"]))
              
        else:
            print("Öğrenci Kayıtlı Değil!")
                       
        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")    

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() != "e":                        
               print("Görüşmek Üzere...")
               kaydet(ogrenciler)
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
                       ogrenci["ad"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                       while len(ogrenci["ad"])<2:
                         print("Lütfen isim giriniz")
                         ogrenci["ad"] = input("İsim:\n--> ").upper()
                       while not ogrenci["ad"].isalpha():
                        print("Lütfen isim giriniz")
                        ogrenci["ad"] = input("İsim:\n--> ").upper()
                       print("Başarıyla değiştirildi")

                    elif değiştir == "soyisim":
                       ogrenci["soyad"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                       while len(ogrenci["soyad"])<=2:
                         print("Lütfen soyisim giriniz")
                         ogrenci["soyad"] = input("Soyisim:\n--> ").upper()
                       while not ogrenci["soyad"].isalpha():
                        print("Lütfen soyisim giriniz")
                        ogrenci["soyad"] = input("Soyisim:\n--> ").upper()
                       print("Başarıyla değiştirildi")

                    elif değiştir == "yaş":
                        ogrenci["yas"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                        while int(ogrenci["yas"])<=2:
                         print("Lütfen Yaş giriniz")
                         ogrenci["yas"] = input("Yaş:\n--> ").upper()
                        while not ogrenci["yas"].isdigit():
                         print("Lütfen yaş giriniz")
                         ogrenci["yas"] = input("Yaş:\n--> ").upper()
                        print("Başarıyla değiştirildi")
                    
                    elif değiştir == "bölüm":
                        ogrenci["bölüm"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                        while ogrenci["bölüm"] not in bölümler:
                            print("Lütfen doğru bölüm girin")
                            ogrenci["bölüm"] = input("Bölüm:\n--> ").upper()
                        print("Başarıyla değiştirildi")
                        
                    elif değiştir == "okul numarası":
                        ogrenci["numara"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                        while ogrenci["numara"]<=2:
                         print("Lütfen Numara giriniz")
                         ogrenci["numara"] = input("Numara:\n--> ").upper()
                        while not ogrenci["numara"].isdigit():
                         print("Lütfen yaş giriniz")
                         ogrenci["numara"] = input("Numara:\n--> ").upper()
                        print("Başarıyla değiştirildi")

                    elif değiştir == "cinsiyet":
                        ogrenci["cinsiyet"] = input("Yeni bilgiyi giriniz:\n-->").upper()
                        while not (cinsiyet.lower()=="erkek" or cinsiyet.lower()=="kadın"):
                            print("Lütfen Cinsiyeti Erkek veya Kadın olarak belirleyin")
                            ogrenci["cinsiyet"] = input("Cinsiyeti:\n--> ").upper()
                    else:
                        print("Yanlış işlem girildi")


        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):\n-->")    

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() != "e":                        
               print("Görüşmek Üzere...")
               kaydet(ogrenciler)
               break            
    
                    
        else:
            print("Öğrenci Kayıtlı Değil!")


    else:
        print("Yanlış İşlem girdiniz lütfen dikkat edin!")    
