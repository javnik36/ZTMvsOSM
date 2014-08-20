def sortuj(plik):
    import json
    import re

    plik1 = open(plik, 'r', encoding="utf-8")

    data = plik1.read()
    plik1.close()


    decoded = json.loads(data)


    stop_position = []
    bad_stop_position = []

    bus_stop = []
    tram_stop = []
    bad_stop = []

    platform = []
    rail_platform = []
    bad_platform = []

    error = []


    for item in decoded:
        if re.search("node/", item["id"]):
            itag = item["properties"]
            itag.setdefault("ref")
            itag.setdefault("name")
            
            if itag.get("public_transport") != None:
                if itag.get("public_transport") == "stop_position":
                    stop_position.append(item)
                else:
                    bad_stop_position.append(item)            
            elif itag.get("highway") != None:
                if itag.get("highway") == "bus_stop":
                    bus_stop.append(item)
                else:
                    bad_stop.append(item)
            elif itag.get("railway") != None:
                if itag.get("railway") == "tram_stop":
                    tram_stop.append(item)
                else:
                    bad_stop.append(item)
        elif re.search("way/", item["id"]):
            itag = item["properties"]
            itag.setdefault("ref")
            itag.setdefault("name")

            if itag.get("public_transport") != None:
                if itag.get("public_transport") == "platform":
                    platform.append(item)
                else:
                    bad_platform.append(item)            
            elif itag.get("railway") != None:
                if itag.get("railway") == "platform":
                    rail_platform.append(item)
                else:
                    bad_platform.append(item)

        else:
            error.append(item)
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...błąd szukania!")
            continue

    print("Sortowanie skończone! Wyniki:")
    print(str(len(stop_position)) + ' dobrych stop_position')
    print(str(len(bus_stop)) + ' dobrych bus_stop')
    print(str(len(tram_stop)) + ' dobrych tram_stop')
    print(str(len(platform)) + ' dobrych platform')
    print(str(len(rail_platform)) + ' dobrych rail_platform')
    print(str(len(bad_stop_position)) + ' złych stop_position')
    print(str(len(bad_stop)) + ' złych stop')
    print(str(len(bad_platform)) + ' złych platform')
    print(str(len(error)) + ' błędów')
