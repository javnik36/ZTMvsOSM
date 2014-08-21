def make_json(variable, nazwa_pliku):
    '''(var, str) -> None
    Zapisuje zmienną (variable) do ścieżki \web\nazwa_pliku.

    '''
    import json

   
##    while how_many != 0:
##        filename = input("Podaj nazwę pliku do którego mam zapisać? (dodaj '.geojson' na końcu!)")
##        plik = open(filename, 'w')
##        print("success")
##        variable = input("Podaj zmienną z której mam zapisać...")
##        zapis = json.JSONEncoder().encode(variable)
##        plik.write(zapis)
##        plik.close()
##
##        how_many -= 1
    
    
    if len(variable) != 0:
        zapis = json.JSONEncoder().encode(variable)
        path = '.\web\/' + nazwa_pliku
        plik = open(path , 'w', encoding="utf-8")
        intro = '''{ "type": "FeatureCollection", "features": '''
        plik.write(intro)
        plik.write(zapis)
        plik.write("}")
