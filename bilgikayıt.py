ogrenciler = []
while True:
    islem = input("\nİşlem türü seçiniz:\n1)Öğrenci Kayıt\n2)Öğrenciler\n3)öğrenci Sorgu\n-->")   #İşlem türünü seçtir

    if islem.lower() == "öğrenci kayıt" :                                          #Eğer işlem öğrenci kayıt ise değişkenleri girmesini iste

        ad = input("İsim: ")              #Ad değişkeni
        soyad = input("Soyisim: ")        #SoyAd değişkeni
        yas = input("Yaş: ")              #yas değişkeni
        bölüm = input("Bölüm: ")          #bölüm değişkeni
        numara = input("Okul Numarası: ") #numara değişkeni

        ogrenci = {"ad": ad, "soyad": soyad, "yas": yas, "bölüm": bölüm, "numara": numara}  #ogrenci listesinde diziye isim ver ve her isime değişken ata

        ogrenciler.append(ogrenci)                                                          #ogrencideki bilgileri tek tek ogrenciler listesine kayıt et

        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")                         #Devam etmek istiyormu diye sor

        if devam.lower() != "e":                                                            #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et,
            print("Görüşmek Üzere...")
            break

    elif islem.lower() == "öğrenciler" :                                                     #Eğer işlem öğrencilerse çalıştır

        if len(ogrenciler) != 0:
            for ogrenci in ogrenciler:                                                          #ogrenciler listesindeki her değer için ogrenciyi değiştir ve str atanan değişkenleri formatla yazdır
                print("\nAdı: {} \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"]))

        elif len(ogrenciler) == 0:
            print("Kayıtlı Öğrenci Yok")       

        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")    #Devam etmek istiyormu diye sor

        if devam.lower() != "e":                                       #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
              print("Görüşmek Üzere...")
              break
        

    elif islem.lower() == "öğrenci sorgu" :                  #eğer işlem öğrenci sorguysa çalıştır

        numara = input("Öğrencinin numarasını giriniz: ")   #aranan öğrencinin numarasını iste
        if len(ogrenciler) == 0:
            print("Öğrenci Kayıtlı Değil!")

        elif numara == ogrenci["numara"]:    
            for ogrenci in ogrenciler:                          #ogrenciler listesindeki her değer için ogrenciyi değiştir
              print("\nAdı: {}  \nSoyadı: {} \nYaşı: {} \nBölümü: {} \nOkul Numarası: {}\n".format(ogrenci["ad"], ogrenci["soyad"], ogrenci["yas"], ogrenci["bölüm"], ogrenci["numara"]))
              
        else:
            print("Öğrenci Kayıtlı Değil!")
              
                   
        
                 

        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")    #Devam etmek istiyormu diye sor

        if devam.lower() != "e":                                           #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
               print("Görüşmek Üzere...")
               break

        

    else:
        print("Yanlış İşlem girdiniz lütfen dikkat edin!")    
