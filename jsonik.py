import json
import re

plik1 = open("export.geojson", 'r', encoding="utf-8")
plik2 = open("przystanki_ktotka_nazwa.txt", 'r')


data = plik1.read()
plik1.close()

decoded = json.loads(data)

existed = []
not_ref = []

for jsonek in decoded:
    item = jsonek
    try:
        tagi = item["tags"]
        existed.append(tagi["ref"])
    except:
        ids = item["id"]
        not_ref.append(ids)
        print("Not fouded!")
        pass

lista_id = []

for line in plik2:
    find = re.search("^[0-9]{6}", line)
    add = find.group()
    lista_id.append(str(add))

plik2.close()

not_in_ztm = []

for key in existed:
    if key in lista_id:
        pass
    else:
        not_in_ztm.append(key)

not_existed = []

for key in lista_id:
    if key in existed:
        pass
    else:
        not_existed.append(key)
