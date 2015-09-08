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

    inp = open(plik_ztm, 'r', encoding="windows-1250")
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


def make_gps(plik_we, plik_wy):
  '''(txt) -> gpx
  Tworzy gpx z pliku input zawierającego przystanki do gpx
  '''
  import gpxpy.gpx as gpx

  wejscie = open(plik_we, 'r')

  plik = gpx.GPX()

  for line in wejscie:
    line = line.split(', ')
    wpt = gpx.GPXWaypoint(line[1], line[2], name = line[0])
    plik.waypoints.append(wpt)

  wejscie.close()
  wyjscie = open(plik_wy, 'w', encoding = "utf-8")
  wyjscie.write(plik.to_xml())
  wyjscie.close()
  print("Stworzono gpx!")
