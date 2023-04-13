ogrenciler = []
bölümler = ["yazılım","hukuk","muhasebe","dijitaliçerik","matbaa"]
while True:
    #İşlem türünü seçtir
    islem = input("\nİşlem türü seçiniz:\n1)Öğrenci Kayıt\n2)Öğrenciler\n3)öğrenci Sorgu\n-->")   

    #Eğer işlem öğrenci kayıt ise değişkenleri girmesini iste
    if islem.lower() == "öğrenci kayıt":  

        #İstediğimiz Değişkenler ve değişken türü koruması
        #While not kodu ile istediğimiz değişkeni veya girişi zorunlu kılıyoruz
        ad = input("İsim: ")
        while len(ad)<=2:
            print("Lütfen isim giriniz")
            ad = input("İsim: ")
        while not ad.isalpha():
            print("Lütfen isim giriniz")
            ad = input("İsim: ")

        soyad = input("Soyisim: ")
        while len(ad)<=1:
            print("Lütfen soyisim giriniz")
            soyad = input("Soyisim: ")
        while not soyad.isalpha():
            print("Lütfen soyisim giriniz")
            soyad = input("Soyisim: ")

        yas = input("Yaş: ")
        while int(yas)<=17:
            print("Yaş en az 18 olabilir")
            yas = input("Yaş: ") 
        while not yas.isdigit():
            print("Lütfen Sayı giriniz")
            yas = input("Yaş: ")

        bölüm = input("Bölüm: ")
        while bölüm.lower() not in bölümler:
             print("Lütfen doğru bölüm girin")
             bölüm = input("Bölüm: ")

        while not bölüm.isalpha():
            print("Lütfen bölüm giriniz")
            bölüm = input("Bölüm: ")

        numara = input("Okul Numarası: ")
        while not numara.isdigit():
            print("Lütfen Sayı giriniz")
            numara = input("Okul Numarası: ")

        cinsiyet = input("Cinsiyeti: ")
        while not (cinsiyet.lower()=="erkek" or cinsiyet.lower()=="kadın"):
            print("Lütfen Cinsiyeti Erkek veya Kadın olarak belirleyin")
            cinsiyet = input("Cinsiyeti: ")

        #ogrenci listesinde diziye isim ver ve her isime değişken ata
        ogrenci = {"ad": ad.upper(), "soyad": soyad.upper(), "yas": yas, "bölüm": bölüm.upper(), "numara": numara,"cinsiyet":cinsiyet.upper()}  

        #ogrencideki bilgileri tek tek ogrenciler listesine kayıt et
        ogrenciler.append(ogrenci) 

        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() == "e":                        
            continue
        elif devam.lower() == "h":
            print("Görüşmek üzere")
            break

    #Eğer işlem öğrencilerse çalıştır
    elif islem.lower() == "öğrenciler" :                                                     

        if len(ogrenciler) != 0:
            for ogrenci in ogrenciler: 

                #ogrenciler listesindeki her değer için ogrenciyi değiştir ve str atanan değişkenleri formatla yazdır
                print("\nAdı: {} \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"]))
 
        #ogrenci karakter uzunluğu 0 ise öğrenci kayıdı yoktur de
        elif len(ogrenciler) == 0:
            print("Kayıtlı Öğrenci Yok")       
        
        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")    

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() != "e":                   
              print("Görüşmek Üzere...")
              break
        
    #eğer işlem öğrenci sorguysa çalıştır
    elif islem.lower() == "öğrenci sorgu" :   

        #aranan öğrencinin numarasını iste
        numara = input("Öğrencinin numarasını giriniz: ")  

        #ogrenciker karakter uzunluğu 0 ise öğrenci kayıdı yoktur de
        if len(ogrenciler) == 0:
            print("Öğrenci Kayıtlı Değil!")

        #ogrenciler listesindeki her değer için ogrenciyi değiştir
        elif len(ogrenciler) != 0:   
            for ogrenci in ogrenciler:
                if numara in ogrenci["numara"]:                          
                    print("\nAdı: {}  \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\nCinsiyeti: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"],ogrenci["cinsiyet"]))
              
        else:
            print("Öğrenci Kayıtlı Değil!")
                       
        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")    

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() != "e":                        
               print("Görüşmek Üzere...")
               break

        

    else:
        print("Yanlış İşlem girdiniz lütfen dikkat edin!")    
