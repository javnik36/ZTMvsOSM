import json

plik1 = open("export-small.geojson", 'r', encoding="utf-8")
plik2 = open("przystanki_krotka_nazwa.txt", 'r')


data = plik1.read()
plik.close()

decoded = json.loads(data)


lista_id = []

for line in plik2:
    add = re.match("[0-9]{6}", line)
    lista_id.append(add)

plik2.close()
