harfler = input("Harfleri girin?")
print(list (harfler))

kelimeler = ['AB','AÇ','AD','AF','AĞ','AH','AK','AL','AM','AN','AR','AS','AŞ','AT','AV','AY','AZ']

for i in range(len(kelimeler)):
    kelimeler[i] = kelimeler[i].lower()

for kelime in kelimeler:
        hepsi_var = all([harf in harfler for harf in kelime])
        if hepsi_var == True:
            print(kelime)
          
        else:
            continue

#github test

