##Wymaga pliku stopy.txt, który tworzy się po uruchomieniu głównego programu
##Skrypt automatyczny-nie wymaga roboty przy nim ;)
import urllib.request as urllib
import json
import datetime

url = "http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28area%283603509824%29%3Barea%283603014990%29%3Barea%283602603447%29%3Barea%283602719113%29%3Barea%283602603448%29%3Barea%283600336313%29%3Barea%283600336311%29%3Barea%283600336310%29%3Barea%283600336309%29%3Barea%283600336304%29%3Barea%283602101329%29%3Barea%283602996965%29%3Barea%283602996986%29%3Barea%283602997041%29%3Barea%283602996990%29%3Barea%283602415879%29%3Barea%283600336137%29%3Barea%283602416275%29%3Barea%283602416274%29%3Barea%283600336138%29%3Barea%283602996903%29%3Barea%283602924728%29%3Barea%283600336688%29%3Barea%283600336679%29%3Barea%283601994190%29%3Barea%283601994189%29%3Barea%283602910919%29%3Barea%283601994191%29%3Barea%283603015006%29%3Barea%283601994186%29%3Barea%283601753833%29%3Barea%283602695156%29%3B%29%2D%3E%2Earea%3B%28node%5B%22highway%22%3D%22bus%5Fstop%22%5D%28area%2Earea%29%3Bnode%5B%22railway%22%3D%22tram%5Fstop%22%5D%28area%2Earea%29%3Bnode%5B%22public%5Ftransport%22%3D%22stop%5Fposition%22%5D%28area%2Earea%29%3Bnode%5B%22public%5Ftransport%22%3D%22platform%22%5D%28area%2Earea%29%3Bway%5B%22public%5Ftransport%22%3D%22platform%22%5D%28area%2Earea%29%3B%29%3Bout%20body%3B%3E%3Bout%20skel%3B"
path = 'data_for_stats.geojson'
urllib.urlretrieve(url, path)


plik = open(path, 'r', encoding="utf-8")
data = plik.read()
plik.close()

decoded = json.loads(data)

dane = decoded["elements"]

osm_stops_ref = 0
osm_stops = 0
osm_pos = 0
osm_pos_ref = 0
osm_plat = 0
osm_plat_ref = 0
err = 0


for item in dane:
    try:
        tagi = item["tags"]
        tagi.setdefault("ref")
        tagi.setdefault("name")
        
        if tagi.get("public_transport") != None:
            if tagi.get("public_transport") == "stop_position":
               if tagi.get("ref") != None:
                   osm_pos_ref += 1
               else:
                   osm_pos += 1
            elif tagi.get("public_transport") == "platform":
                if tagi.get("ref") != None:
                   osm_plat_ref += 1
                else:
                   osm_plat += 1
            else:
                err += 1
        elif tagi.get("highway") != None:
            if tagi.get("highway") == "bus_stop" or tagi.get("railway") == "tram_stop":
                if tagi.get("ref") != None:
                   osm_stops_ref += 1
                else:
                   osm_stops += 1
            else:
                err += 1
        else:
            #print("hę?")
            continue

    except:
        continue

    
#############
ztm_stops = 0
p2 = "stopy.txt"
file = open(p2, 'r')

for line in file:
    if line != 0:
        ztm_stops += 1
    else:
        continue
file.close()

#############
print("RAPORT.......................................................:")
print("Wszystkich przystanków w bazie ztm:                          :" + str(ztm_stops))
print("Wszystkich przystanków(bus/tram_stop) w bazie osm            :" + str(osm_stops+osm_stops_ref))
print("                                                       z tego:" + str(osm_stops_ref) + " z REFem")
print("Wszystkich pozycji postojowych(stop_position) w bazie osm    :" + str(osm_pos+osm_pos_ref) + " czyli          " + str(((osm_pos+osm_pos_ref)/ztm_stops)*100) + "%")
print("                                                       z tego:" + str(osm_pos_ref) + " z REFem. Czyli " + str((osm_pos_ref/(osm_pos+osm_pos_ref))*100) + "% wszystkich stop_position")
print("Wszystkich platform w bazie osm                              :" + str(osm_plat+osm_plat_ref) + " czyli          " + str(((osm_plat+osm_plat_ref)/ztm_stops)*100) + "%")
print("                                                       z tego:" + str(osm_plat_ref) + " z REFem. Czyli " + str((osm_plat_ref/(osm_plat+osm_plat_ref))*100) + "% wszystkich platform")
print("Błędów                                                       :" + str(err))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#############
p3 = 'statystyki.txt'
save = open(p3 , 'a')

save.write(datetime.datetime.now().strftime("%d.%m.%y  %H:%M") + '\n')
save.write(str(ztm_stops) + '\n')
save.write(str(osm_stops+osm_stops_ref) + '\n')
save.write(str(osm_stops_ref) + '\n')
save.write(str(osm_pos+osm_pos_ref) + '\n')
save.write(str(osm_pos_ref) + '\n')
save.write(str(osm_plat+osm_plat_ref) + '\n')
save.write(str(osm_plat_ref) + '\n')
save.write("###################\n")
save.close()
