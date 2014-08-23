ZTMvsOSM
-------------
![Demo][/master/demo.png]

Program sprawdza braki w przystankach między podanym geojsonem a bazą ZTMu i tworzy pliki .geojson z zaznaczonymi brakami, które można podejrzeć na leaflecie.

Jak uruchomić?
-------------
Potrzebujesz Pythona3.<br>
1. Pobierz całą zawartość githuba.<br>
2. Pobierz z overpassa plik geojson z bazą przystanków(export > geojson) i zapisz go w folderze głównym programu. Tutaj mój link: http://overpass-turbo.eu/s/4Hh<br>
3. Pobierz z [ZTMu plik z rozkładami](ftp://rozklady.ztm.waw.pl/) i rozpakuj go do folderu głównego programu.<br>
4. Uruchom skrypt ZTMvsOSM.py i podążaj za wskazówkami ;)<br>
5. Na ostatnie pytanie odpowiedz 't'<br>
6. Uruchom przeglądarkę i otwórz stronę<br>
```
http://localhost:8000/web/index.html
```
I...'Baw się' zawartością!

~~PS. Dla leniwych opublikuję niedługo pliki json z tą samą zawartością. Będzie można chociaż przez githuba podejrzeć.~~

Szczegóły
-------------
- od z16 pojawią się przycisk edycji obszaru w edytorze osm
- program tworzy czasowy serwer lokalny, żeby można było przeglądać mapę. Z jakiegoś powodu bez tego zabiegu nie działa wczytywanie zew. geojson-ów (przynajmniej w Chrome)
- program sprawdza całą bazę przystanków, więc jak wgrasz ich mniej(np. samą Warszawę) to pokaże potem braki poza Warszawą, mimo że te przystanki mogą być w osm (po prostu nie będzie ich geojsonie)
- nie jestem programistą więc błędów pewnie sporo, nawet w danych wyjściowych więc mapki traktować trochę z przymrużeniem oka...nie ufać im na 100% :)
- wiem, że cały proces może być dość upierdliwy i czasochłonny, ale nie mam chwilowo werwy, żeby przepisać kod na taki, żeby był bardziej bezobsługowy

[extract.py](../blob/master/extract.py)
-------------
Niektórym może się przydać sam extract.py. Dane z ztmu przekształca do formatu:
```
##
ID PRZYSTANKU, SZEROKOŚĆ GEO, DŁUGOŚĆ GEO
100503, 52.259210, 21.025190
...
##
```
Może być pomocne przy dalszej obróbce.

Wykorzystane:
-------------
* [Leaflet](http://leafletjs.com/) (C) 2010-2014, Vladimir Agafonkin; 2010-2011, CloudMade
* [EditInOSM](https://github.com/yohanboniface/Leaflet.EditInOSM) (C) 2014 Yohan Boniface <yb@enix.org> 
* [leaflet-ajax](https://github.com/calvinmetcalf/leaflet-ajax) (c) 2012-2013 Calvin Metcalf 

Mój kod:
-------------
[Copyright (c) 2014 javnik36][]

[Copyright (c) 2014 javnik36][https://github.com/javnik36/ZTMvsOSM/blob/master/licence]