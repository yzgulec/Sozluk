harfler = input("Harfleri girin?")
print(list (harfler))

import json

#json dosyasını açıyoruz
with open('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\gts5.json',encoding="utf8") as f:
   data = json.load(f)

# harfler listesindeki her bir harfin sayısını hesaplıyorum
harfler_harf_sayisi = {}
for i in harfler:
    harfler_harf_sayisi[i] = harfler.count(i)
# tamamen saglama amacli yazdiriyorum    
#print(harfler_harf_sayisi)

#json dosyasındaki her bir kelimeyi kelimeler listesine ekliyorum. json dosyasindaki (yani sozlukteki) madde key'ine karsilik gelen her value bizim icin kelimedir.
kelimeler = []

for i in range(len(data)):
    
        kelimeler.append(data[i]['madde'])
#kelimeler listesindeki duplicate kayitlari ucuruyoruz
kelimeler = list( dict.fromkeys(kelimeler) )
        

#harflerdeki her harf ayni zamanda kelimede mevcut mu kontrolü burada yapiyoruz
for kelime in kelimeler:
        hepsi_var = all([harf in harfler for harf in kelime])
        if hepsi_var == True:
         
            #her bir kelimedeki harf sayisini hesapliyorum
            kelime_harf_sayisi = {}
            for i in kelime:
                kelime_harf_sayisi[i] = kelime.count(i)
            #print(kelime_harf_sayisi)
            #print(harfler_harf_sayisi)
            
            #bir kelimenin gecerli olabilmesi icin harfler listesindeki spesifik bir harfin toplam bulunma sayisi kelimeler listesindeki aynı harfin sayisindan kucuk veya esit olmali
            if kelime.count(i) <= harfler.count(i):  
    
                print(kelime)
                   
                
        else:
            continue



