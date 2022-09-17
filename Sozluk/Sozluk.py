﻿harfler = input("Harfleri girin?")
print(list (harfler))

import json

#json dosyasını açıyoruz
with open('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\gts5.json',encoding="utf8") as f:
   data = json.load(f)

# harfler listesindeki her bir harfin sayısını hesaplıyorum
harfler_harf_sayisi = {}
for i in harfler:
    harfler_harf_sayisi[i] = harfler.count(i)

#json dosyasındaki her bir kelimeyi kelimeler listesine ekliyorum. json dosyasindaki (yani sozlukteki) madde key'ine karsilik gelen her value bizim icin kelimedir.
kelimeler = []
for i in range(len(data)):
    kelimeler.append(data[i]['madde'])

#kelimeler listesindeki duplicate kayitlari ucuruyoruz
kelimeler = list(dict.fromkeys(kelimeler))


#harflerdeki her harf ayni zamanda kelimede mevcut mu kontrolü burada yapiyoruz
for kelime in kelimeler:
        hepsi_var = all([harf in harfler for harf in kelime])
 
        #her bir kelimedeki harf sayisini hesapliyorum
        kelime_harf_sayisi = {}
        for i in kelime:
                kelime_harf_sayisi[i] = kelime.count(i)     
        
        if hepsi_var == True:  
    
                #bu nokta çok kritik. burada kelimenin gecerli olabilmesi icin harflerdeki harf sayisinin kelimedeki harf sayisindan olması gerektigini soyluyoruz
                gecerli_kelime = all(harfler_harf_sayisi[k] >= kelime_harf_sayisi[k] for k in kelime_harf_sayisi) and (len(kelime_harf_sayisi) > 1)
                
                ''' kelimedeki harf sayısının harflerdeki harf sayısına eşit veya kücük mü doğrulamasını burada yapabiliriz
                print(gecerli_kelime)
                print(kelime)
                '''
                if gecerli_kelime == True:
                    print(kelime)

        else:
            continue



