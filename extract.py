def extract(plik_ztm, plik_wyjsciowy):
    '''(txt) -> txt
    PAMIĘTAJ O ROZSZERZENIU!
    
    Z podanego pliku ztm tworzy plik o schemacie:
    ##
    ID PRZYSTANKU, SZEROKOŚĆ GEO, DŁUGOŚĆ GEO
    100503, 52.259210, 21.025190
    ...
    ##
    '''
    import re

    inp = open(plik_ztm, 'r')
    out = open(plik_wyjsciowy, 'w')

    print("Zaczynam!")
    for line in inp:
        pattern = "^\s+(\d{6}).{94}\Y=\s(\d{2}\.\d{6})\s+\X=\s(\d{2}\.\d{6})"
        macz = re.search(pattern, line)
          
        if macz:
            out.write(macz.group(1) + ', ' + macz.group(2) + ', ' + macz.group(3) + "\n")
            #print("Znalazłem!")
        else:
            continue

    inp.close()
    out.close()
    print("Zakończono wyodrębnianie!")
