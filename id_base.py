def make_id_base(plik, zmienna_listy):
    import re

    read = open(plik, 'r')
    

    for line in read:
        find = re.search("^[0-9]{6}", line)
        add = find.group()
        zmienna_listy.append(str(add))
