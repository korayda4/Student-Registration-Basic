ogrenciler = []
while True:
    #İşlem türünü seçtir
    islem = input("\nİşlem türü seçiniz:\n1)Öğrenci Kayıt\n2)Öğrenciler\n3)öğrenci Sorgu\n-->")   

    #Eğer işlem öğrenci kayıt ise değişkenleri girmesini iste
    if islem.lower() == "öğrenci kayıt":  

        #İstediğimiz Değişkenler
        ad = input("İsim: ")             
        soyad = input("Soyisim: ")        
        yas = input("Yaş: ")              
        bölüm = input("Bölüm: ")          
        numara = input("Okul Numarası: ") 
        cinsiyet = input("Cinsiyeti: ")

        #ogrenci listesinde diziye isim ver ve her isime değişken ata
        ogrenci = {"ad": ad, "soyad": soyad, "yas": yas, "bölüm": bölüm, "numara": numara,"cinsiyet":cinsiyet}  

        #ogrencideki bilgileri tek tek ogrenciler listesine kayıt et
        ogrenciler.append(ogrenci) 

        #Devam etmek istiyormu diye sor
        devam = input("Tekrar İşlem yapmak istiyor musunuz?(E/H):")                         

        #Büyük E küçük e ayrımını düzelt ve e ye eşit değilse sonlandır eşitse devam et
        if devam.lower() != "e":                        
            print("Görüşmek Üzere...")
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
