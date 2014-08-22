def make_json(variable, nazwa_pliku):
    '''(var, str) -> None
    Tworzy geojson ze zmiennej (variable) do ścieżki \web\nazwa_pliku.

    '''
    import json
    
    if len(variable) != 0:
        zapis = json.JSONEncoder().encode(variable)
        path = '.\web\/' + nazwa_pliku
        plik = open(path , 'w', encoding="utf-8")
        intro = '''{ "type": "FeatureCollection", "features": '''
        plik.write(intro)
        plik.write(zapis)
        plik.write("}")
        print("Geojson stworzony!")
    else:
        print("Brak danych w podanej zmiennej!")

    
