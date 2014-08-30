def make_id_base(plik, zmienna_listy):
    import re

    read = open(plik, 'r')
    

    for line in read:
        find = re.search("^[0-9]{6}", line)
        add = find.group()
        zmienna_listy.append(str(add))


def take(baza_id, plik, json_output, json_output_temporary):
    '''
    Tworzy bazę brakujących przystanków w osm i bazę przystanków tymczasowych.
    '''
    import re

    zapis = []
    temp = []
    
    
    file = open(plik, 'r')
    data = file.readlines()
    file.close()

    
    for line in data:
        find = re.search("^[0-9]{6}", line)
        add = find.group()
        if add in baza_id:
            if add.isnumeric() and not re.search("^\d{4}5\d", add):
                zapis.append(line)
            else:
                temp.append(line)
        else:
            continue

    
    for item in zapis:
        splitted = []
        splitted = item.split(', ')

        dicta = {"type":"Feature", "properties" : {"ref":splitted[0] }, "geometry": {"type":"Point","coordinates": [float(splitted[2].rstrip("\n")), float(splitted[1])] }}
        
        #save = '''[{"type":"Feature"},"geometry":{"type":"Point","coordinates":[''' + splitted[1] + "," + splitted[2].rstrip("\n") + "]}}"

        json_output.append(dicta)

    for item in temp:
        splitted = []
        splitted = item.split(', ')

        dicta = {"type":"Feature", "properties" : {"ref":splitted[0] }, "geometry": {"type":"Point","coordinates": [float(splitted[2].rstrip("\n")), float(splitted[1])] }}
        
        json_output_temporary.append(dicta)
