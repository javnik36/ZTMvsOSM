import json
import re

plik1 = open("export-small.geojson", 'r', encoding="utf-8")
plik2 = open("przystanki_ktotka_nazwa.txt", 'r')


data = plik1.read()
plik1.close()

decoded = json.loads(data)


lista_id = []

for line in plik2:
    find = re.search("^[0-9]{6}", line)
    add = find.group()
    lista_id.append(str(add))

plik2.close()
