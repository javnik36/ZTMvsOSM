import id_base as t1
import sorter as t2

def checker(baza_id, stop_position, bez_ref, small_ref):
    '''Sprawdza obecność tagów ref i name na listach z sortera

    '''

    import re
    #import sorter

    #base = baza_id

    

    for item in stop_position:
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
                print("usu")
            except:
                continue

baza = []

stop_position = []
bad_stop_position = []

bus_stop = []
tram_stop = []
bad_stop = []

platform = []
rail_platform = []
bad_platform = []

error = []

bez_ref = []
small_ref = []



t1.make_id_base("przystanki_ktotka_nazwa.txt", baza)
print(len(baza))
t2.sortuj("export-big.geojson", stop_position, bad_stop_position, bus_stop, tram_stop, bad_stop, platform,rail_platform, bad_platform, error)
checker(baza, stop_position, bez_ref, small_ref)
print(len(baza))
