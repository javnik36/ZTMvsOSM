ZTMvsOSM
-------------
![Demo][demo.png]

Program sprawdza braki w przystankach między podanym geojsonem a bazą ZTMu i tworzy htmla z zaznaczonymi brakami.

Jak uruchomić?
-------------
1. Pobierz całą zawartość githuba
2. Pobierz z overpassa plik geojson z bazą przystanków(export > geojson) i zapisz go w folderze głównym programu. Tutaj mój link: http://overpass-turbo.eu/s/4Hh
3. Pobierz z [ZTMu plik z rozkładami](ftp://rozklady.ztm.waw.pl/) i zapisz go w folderze głównym programu.
4. Uruchom skrypt ZTMvsOSM.py i podążaj za wskazówkami ;)
5. Na ostatnie pytanie odpowiedz 't'
6. Uruchom przeglądarkę i otwórz stronę
'''
http://localhost:8000/web/index.html

'''
7. 'Baw się' zawartością!

PS. Dla leniwych opublikuję niedługo pliki json z tą samą zawartością. Będzie można chociaż przez githuba podejrzeć.

Szczegóły
-------------
- od z16 pojawią się przycisk edycji obszaru w edytorze osm
- nie jestem programistą więc błędów pewnie sporo, nawet w danych wyjściowych więc mapki traktować trochę z przymrużeniem oka...nie ufać im na 100% :)

[extract.py](../extract.py)
-------------
Niektórym może się przydać sam extract.py. Dane z ztmu przekształca do formatu:
'''
##
ID PRZYSTANKU, SZEROKOŚĆ GEO, DŁUGOŚĆ GEO
100503, 52.259210, 21.025190
...
##
'''
Może być pomocne przy dalszej obróbce.

Wykorzystane:
-------------
* (C) 2010-2014, Vladimir Agafonkin; 2010-2011, CloudMade [Leaflet](http://leafletjs.com/)
* (C) 2014 Yohan Boniface <yb@enix.org> [EditInOSM](https://github.com/yohanboniface/Leaflet.EditInOSM)
* (c) 2012-2013 Calvin Metcalf [leaflet-ajax](https://github.com/calvinmetcalf/leaflet-ajax)