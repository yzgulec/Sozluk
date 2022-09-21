def harfgiris():

    harfler = (input("Harfleri girin?" + ' ')).lower()
    global ilebaslayan_harfler, ilebiten_harfler
    ilebaslayan_harfler=str(input("Hangi harf ile başlasın?"))
    ilebiten_harfler=str(input("Hangi harf ile bitsin?"))
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

    #kelimeler'i alfabetik sıraya göre ve her bir kelimenin sahip olduğu karakter sayısına sıralıyoruz  
    kelimeler=sorted(sorted(kelimeler),key=len)

    #kelimeler listesindeki duplicate kayitlari ucuruyoruz
    kelimeler = list(dict.fromkeys(kelimeler))
    
    kelimelistesi_harfsayili=""
    global kelimelistesi_array
    kelimelistesi_array=[]

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
                        
                            kelimelistesi_harfsayili=kelimelistesi_harfsayili + (str(len(kelime)) + ' ' + 'harfli: ' + kelime + "\n")
                            
                            #burada tüm geçerli kelimeleri bir array listesinde topluyorum
                            kelimelistesi_array.append(kelime)
                            
        else:
            continue

    #olası tüm kelimeleri yazdırıyoruz
    print(kelimelistesi_harfsayili)
    #print(kelimelistesi_array)

    #belli bir harf ile başlayan veya kelimeler icin filtre
    ilebaslayan_kelime_harfsayili=""
    ilebaslayan_kelimeler = [x for x in kelimelistesi_array if x.startswith(ilebaslayan_harfler)]
    
    if (ilebaslayan_harfler) and (not ilebiten_harfler):
        print("ile baslayan kelimeler : " + str(ilebaslayan_kelimeler))
        for ilebaslayan_kelime in ilebaslayan_kelimeler:

            ilebaslayan_kelime_harfsayili=ilebaslayan_kelime_harfsayili + (str(len(ilebaslayan_kelime)) + ' ' + 'harfli: ' + ilebaslayan_kelime + "\n")
 
    print(ilebaslayan_kelime_harfsayili)

    #belli bir harf ile biten kelimeler icin filtre
    ilebiten_kelime_harfsayili=""
    ilebiten_kelimeler = [x for x in kelimelistesi_array if x.endswith(ilebiten_harfler)]

    if (ilebiten_harfler) and (not ilebaslayan_harfler):
        print("ile biten kelimeler : " + str(ilebiten_kelimeler))
        for ilebiten_kelime in ilebiten_kelimeler:
        
            ilebiten_kelime_harfsayili=ilebiten_kelime_harfsayili + (str(len(ilebiten_kelime)) + ' ' + 'harfli: ' + ilebiten_kelime + "\n")

    print(ilebiten_kelime_harfsayili)

    #belli bir harf ile başlayıp belli bir harf ile biten kelimeler icin filtre
    ilebaslayip_ilebiten_kelime_harfsayili=""
    if (ilebaslayan_harfler) and (ilebiten_harfler):

        #iki listedeki ortak kelimeleri bir değişkene atıyorum
        ilebaslayip_ilebiten_kelimeler = set(ilebaslayan_kelimeler) & set(ilebiten_kelimeler)
        for ilebaslayip_ilebiten_kelime in ilebaslayip_ilebiten_kelimeler:
            
            ilebaslayip_ilebiten_kelime_harfsayili=ilebaslayip_ilebiten_kelime_harfsayili + (str(len(ilebaslayip_ilebiten_kelime)) + ' ' + 'harfli: ' + ilebaslayip_ilebiten_kelime + "\n")
    print(ilebaslayip_ilebiten_kelime_harfsayili)
    
sonuc()