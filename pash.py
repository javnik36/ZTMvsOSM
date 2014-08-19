#Robi z perla doVisual
#plik txt o patternie:
#ID, LON, LAT
#


import re

plik = open("przystanki_dluga_nazwa.txt", 'r')
save = open("przystanki_ktotka_nazwa.txt", 'w')



for line in plik:
    macz = re.search("^[0-9]{6}", line)
    macz2 = re.search("(\s[0-9]{2}\.[0-9]{6})\,(\s[0-9]{2}\.[0-9]{6})", line)
    if macz:
        save.write(macz.group())
        save.write(',')
    elif macz2:
        save.write(macz2.group())
        save.write("\n")
        print("Dodano stringi!")

plik.close()
save.close()
print("Gotowe")
