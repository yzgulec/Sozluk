def harfgiris():

    harfler = (input("Harfleri girin?" + ' ')).lower()
    print(list (harfler))
    return harfler

def sonuc():
    import json

    #json dosyasını açıyoruz
    with open('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\gts5.json',encoding="utf8") as f:
        data = json.load(f)

    # harfler listesindeki her bir harfin sayısını hesaplıyorum
    harfler=harfgiris()
    harfler_harf_sayisi = {}
    for i in harfler:
        harfler_harf_sayisi[i] = harfler.count(i)

    #json dosyasındaki her bir kelimeyi kelimeler listesine ekliyorum. json dosyasindaki (yani sozlukteki) 'madde' key'ine karsilik gelen her value bizim icin kelimedir.
    kelimeler = []
    for i in range(len(data)):
        kelimeler.append(data[i]['madde'])

    #kelimeler'i alfabetik sıraya göre sıralıyoruz
    kelimeler=sorted(kelimeler)

    #kelimeler listesindeki duplicate kayitlari ucuruyoruz
    kelimeler = list(dict.fromkeys(kelimeler))
    
    kelimelistesi=""
    #harflerdeki her harf ayni zamanda kelimede mevcut mu kontrolü burada yapiyoruz
    for kelime in kelimeler:
        
        hepsi_var = all([harf in harfler for harf in kelime])
        
        #her bir kelimedeki harf sayisini hesapliyorum
        kelime_harf_sayisi = {}
        for i in kelime:
                kelime_harf_sayisi[i] = kelime.count(i)
                
        #harfler listesindeki her harf kelimede de varsa...
        if hepsi_var == True:  
    
                #bu nokta çok kritik. burada kelimenin gecerli olabilmesi icin harflerdeki harf sayisinin kelimedeki harf sayisindan olması gerektigini soyluyoruz. ayrica kelime tek harften oluşuyorsa onu göz ardı ediyoruz.
                gecerli_kelime_sarti = all(harfler_harf_sayisi[k] >= kelime_harf_sayisi[k] for k in kelime_harf_sayisi) and (len(kelime_harf_sayisi) > 1)
                
                
                if gecerli_kelime_sarti == True:
                        
                        #konsola yazdırırken bunu da kullanabilirdik
                        #print(kelime)
                        
                        #olası tüm kelimeleri bir değişkene atıyoruz
                        kelimelistesi=kelimelistesi + "\n" + kelime
                        
                       
        else:
            continue

    #olası tüm kelimeleri yazdırıyoruz
    print(kelimelistesi)
    
sonuc()