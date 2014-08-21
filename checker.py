def checker(baza_id, zmienna_badana, bez_ref, small_ref, bad_name, errors):
    '''Sprawdza obecność tagów ref i name na listach z sortera

    '''

    import re

    przed = len(errors)
    
    for item in zmienna_badana:
        itag = item["properties"]
        ref = itag["ref"]
        name = itag["name"]

        if ref == None:
            bez_ref.append(item)
        elif len(ref) != 6:
            small_ref.append(item)
        elif ref in baza_id:
            try:
                baza_id.remove(ref)
            except:
                continue

        if name == None or not re.search("[0-9]{2}", name):
            bad_name.append(item)
        elif name != None or re.search("[0-9]{2}", name):
            continue
        else:
            errors.append(item)


    print(str(len(bez_ref)) + ' bez refu')
    print(str(len(small_ref)) + ' z za krótkim refem')
    print(str(len(bad_name)) + ' ze złą nazwą')
    print(str(przed - len(errors)) + ' błędów')
