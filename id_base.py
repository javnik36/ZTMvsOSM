def make_id_base(plik, zmienna_listy):
    import re

    read = open(plik, 'r')
    

    for line in read:
        find = re.search("^[0-9]{6}", line)
        add = find.group()
        zmienna_listy.append(str(add))


def take(baza_id, plik, do_jsona):
    import re

    zapis = []
    
    
    file = open(plik, 'r')
    data = file.readlines()
    file.close()

    
    for line in data:
        find = re.search("^[0-9]{6}", line)
        add = find.group()
        if add in baza_id:
            zapis.append(line)
        else:
            continue

    
    for item in zapis:
        splitted = []
        splitted = item.split(', ')

        dicta = {"type":"Feature", "properties" : {"ref":splitted[0] }, "geometry": {"type":"Point","coordinates": [float(splitted[2].rstrip("\n")), float(splitted[1])] }}
        
        #save = '''[{"type":"Feature"},"geometry":{"type":"Point","coordinates":[''' + splitted[1] + "," + splitted[2].rstrip("\n") + "]}}"

        do_jsona.append(dicta)
