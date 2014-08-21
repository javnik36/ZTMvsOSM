import id_base as t1
import sorter as t2
import checker as t3
import save_json as t4


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

bez_ref_stops = []
small_ref_stops = []

bad_name_stops = []

bez_ref_plat = []
small_ref_plat = []

bad_name_plat = []

brak_id = []


t1.make_id_base("przystanki_ktotka_nazwa.txt", baza)
print(len(baza))
t2.sortuj("export-big.geojson", stop_position, bad_stop_position, bus_stop, tram_stop, bad_stop, platform,rail_platform, bad_platform, error)
print("________________________________")
print("Badana zmienna: stop_position") 
t3.checker(baza, stop_position, bez_ref_stops, small_ref_stops, bad_name_stops, error)
print("________________________________")
print("Badana zmienna: bus_stop") 
t3.checker(baza, bus_stop, bez_ref_stops, small_ref_stops, bad_name_stops, error)
print("________________________________")
print("Badana zmienna: tram_stop") 
t3.checker(baza, tram_stop, bez_ref_stops, small_ref_stops, bad_name_stops, error)
print("________________________________")
print("Badana zmienna: platform") 
t3.checker(baza, platform, bez_ref_plat, small_ref_plat, bad_name_plat, error)
print("________________________________")
print(len(baza))
t1.take(baza, "przystanki_ktotka_nazwa.txt", brak_id)
t4.make_json(brak_id, "brak_id.geojson")
#t4.make_json(bez_ref, "bez_ref.geojson")
#t4.make_json(bad_name, "bad_name.geojson")
