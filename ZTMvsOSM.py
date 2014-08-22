import extract as t0
import id_base as t1
import sorter as t2
import checker as t3
import save_json as t4
import server as t5

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
another_error = []

bez_ref_stops = []


bad_name_stops = []

bez_ref_plat = []

small_ref = []

bad_name_plat = []

brak_id = []




t0.extract("RA140825.txt", "stopy.txt")
t1.make_id_base("stopy.txt", baza)
print("________________________________")
#print(len(baza))
t2.sortuj("complete marki.geojson", stop_position, bad_stop_position, bus_stop, tram_stop, bad_stop, platform,rail_platform, bad_platform, error)
print("________________________________")
print("Badana zmienna: stop_position") 
t3.checker(baza, stop_position, bez_ref_stops, small_ref, bad_name_stops, error)
print("________________________________")
print("Badana zmienna: bus_stop") 
t3.checker(baza, bus_stop, bez_ref_stops, small_ref, bad_name_stops, error)
print("________________________________")
print("Badana zmienna: tram_stop") 
t3.checker(baza, tram_stop, bez_ref_stops, small_ref, bad_name_stops, error)
print("________________________________")
print("Badana zmienna: platform") 
t3.checker(baza, platform, bez_ref_plat, small_ref, bad_name_plat, error)
print("________________________________")
print("Badana zmienna: bad_stop_position") 
t3.checker(baza, bad_stop_position, another_error, another_error, another_error, error)
print("________________________________")
#print(len(baza))
t1.take(baza, "przystanki_ktotka_nazwa.txt", brak_id)
t4.make_json(brak_id, "brak_id.geojson")
t4.make_json(bez_ref_stops, "bez_ref_stops.geojson")
t4.make_json(bez_ref_plat, "bez_ref_plat.geojson")
t4.make_json(bad_name_stops, "bad_name_stops.geojson")
t4.make_json(bad_name_plat, "bad_name_plat.geojson")
t4.make_json(another_error, "another_error.geojson")
t4.make_json(small_ref, "small_ref.geojson")

start = input("Wystartować serwer? (t/n) ")
if start == 't':
    t5.server()
else:
    print("Ok...kończę pracę!")
