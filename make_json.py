import json
import re

plik1 = open("export.geojson", 'r', encoding="utf-8")

data = plik1.read()
plik1.close()

decoded = json.loads(data)
i=0
output_data = []
bad_ref = []
bad_name = []

for jsonek in decoded:
    item = jsonek
    itag = item["tags"]
    itag.setdefault("ref")
    itag.setdefault("name")
    slownik = {"id" : item["id"], "lat" : item["lat"], "lon" : item["lon"], "name" : itag["name"], "ref" : itag["ref"]}
    
    if itag.get("public_transport") != None:
        slownik["public_transport"] = itag["public_transport"]
    elif itag.get("highway") != None:
        slownik["highway"] = itag["highway"]


    
    if slownik["ref"] == None:
        bad_ref.append(slownik)
        
    if slownik["name"] == None or not re.search("[0-9]{2}", slownik["name"]) :
        bad_name.append(slownik)


    output_data.append(slownik)
    
    print("Dodano nr. " + str(i) + '!')
    i += 1
    

br = json.JSONEncoder().encode(bad_ref)
bn = json.JSONEncoder().encode(bad_name)
plik2 = open("bad-ref.geojson", 'w')
plik3 = open("bad-name.geojson", 'w')
plik2.write(br)
plik3.write(bn)
plik2.close()
plik3.close()
