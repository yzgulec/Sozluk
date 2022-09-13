harfler = input("Harfleri girin?")
print(list (harfler))

import json

with open('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\gts5.json',encoding="utf8") as f:
   data = json.load(f)

kelime = data[0]['madde']
kelimeler = []

for i in range(len(data)):
    if data[i]['madde']:

        kelimeler.append(data[i]['madde'])


for kelime in kelimeler:
        hepsi_var = all([harf in harfler for harf in kelime])
        if hepsi_var == True:
            print(kelime)
          
        else:
            continue

#github test
